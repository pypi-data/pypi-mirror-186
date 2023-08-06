import os
import pathlib
import queue
import sys
import threading
from datetime import datetime
from time import sleep

import click
import tqdm
from click import pass_context

from rebotics_sdk.cli.common import configure, shell, roles, set_token
from rebotics_sdk.cli.utils import read_saved_role, process_role, ReboticsCLIContext, app_dir, pass_rebotics_context, \
    ReboticsScriptsConfiguration
from rebotics_sdk.providers.fvm import FVMProvider
from .. import utils
from ..advanced import remote_loaders
from ..advanced.packers import VirtualClassificationDatabasePacker
from ..providers import ProviderHTTPClientException, AdminProvider


@click.group()
@click.option('-f', '--format', default='table', type=click.Choice(['table', 'id', 'json']), help='Result rendering')
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode')
@click.option('-c', '--config', type=click.Path(), default='fvm.json', help="Specify what config.json to use")
@click.option('-r', '--role', default=lambda: read_saved_role('fvm'), help="Key to specify what fvm to use")
@click.version_option()
@click.pass_context
def api(ctx, format, verbose, config, role):
    """
    Admin CLI tool to communicate with FVM API
    """
    process_role(ctx, role, 'fvm')
    ctx.obj = ReboticsCLIContext(
        role,
        format,
        verbose,
        os.path.join(app_dir, config),
        provider_class=FVMProvider
    )


api.add_command(shell, 'shell')
api.add_command(roles, 'roles')
api.add_command(configure, 'configure')
api.add_command(set_token, 'set_token')


@api.command(name='file')
@click.option('-f', '--name', required=True, help='Filename of the file', type=click.UNPROCESSED)
@pass_rebotics_context
def virtual_upload(ctx, name):
    """Create virtual upload"""
    if ctx.verbose:
        click.echo('Calling create virtual upload')
    result = ctx.provider.create_virtual_upload(
        name
    )
    if 'id' in result.keys():
        pk = result['id']
        with open(name, 'rb', ) as fio:
            click.echo('Uploading file...')
            remote_loaders.upload(destination=result['destination'], file=fio, filename=name)
            ctx.provider.finish(
                pk
            )
            click.echo("Successfully finished uploading")
    else:
        click.echo("Failed to call virtual upload")


@api.group()
def rcdb():
    pass


def _download_rcdb_locally(ctx, rcdb_file, target):
    rcdb_file = str(rcdb_file)

    if rcdb_file.isdigit():
        # download rcdb file by ID
        try:
            response = ctx.provider.get_rcdb_by_id(int(rcdb_file))
        except ProviderHTTPClientException as exc:
            raise click.ClickException(f"Failed to trigger by API with error: {exc}")
        # should we also save a response? probably no
        return _download_rcdb_locally(ctx, response['file']['file'], target)  # get the url
    elif utils.is_url(rcdb_file):
        # download rcdb file by URL
        filename = utils.get_filename_from_url(rcdb_file)
        local_filepath = pathlib.Path(target / filename)
        if local_filepath.exists():
            return local_filepath
        try:
            remote_loaders.download(rcdb_file, local_filepath)
        except Exception as exc:
            raise click.ClickException(f"Failed to download file by URL: {exc}")
        return _download_rcdb_locally(ctx, local_filepath, target)
    else:
        # assuming that it is a local file path
        local_filepath = pathlib.Path(rcdb_file)
        if not local_filepath.exists():
            raise click.ClickException("Local file is not loaded!")
        return local_filepath


def download_worker(q, provider, progress_bar):
    while True:
        d = q.get()
        if not d:
            break
        url, target = d

        progress_bar.update()
        retries = 0

        while retries < 5:
            try:
                provider.download(url, target)
            except Exception:
                retries += 1
                sleep(retries)
            else:
                break


@rcdb.command(name="unpack")
@click.argument('rcdb_file')
@click.option('-t', '--target', type=click.Path(), default=pathlib.Path('.'))
@click.option('-w', '--with-images', is_flag=True)
@click.option('-c', '--concurrency', default=os.cpu_count(), type=click.INT)
@pass_rebotics_context
def rcdb_unpack(ctx, rcdb_file, target, with_images, concurrency):
    """Unpack rcdb files. if the images """
    target = pathlib.Path(target)
    click.echo("Downloading rcdb file locally...")
    rcdb_file = _download_rcdb_locally(ctx, rcdb_file, target)
    if not with_images:
        click.echo(f"File loaded into {rcdb_file}")
        return

    # create new packer and unpacker
    packer = VirtualClassificationDatabasePacker(
        source=str(rcdb_file),
        with_images=with_images
    )
    features_count = packer.get_features_count()
    click.echo(f"Total features count: {features_count}")

    features_path = target / 'features.txt'
    labels_path = target / 'labels.txt'
    images_path = target / 'images.txt'
    uuids_path = target / 'uuids.txt'

    download_queue = queue.Queue()
    progress_bar = tqdm.tqdm(
        total=features_count,
        desc="Downloading previews..."
    )

    threads = []
    for _ in range(concurrency * 2):
        thread = threading.Thread(
            target=download_worker,
            args=(download_queue, ctx.provider, progress_bar)
        )
        thread.daemon = True
        thread.start()
        threads.append(thread)

    total_images_to_download = 0

    with open(features_path, 'w') as features_io, \
        open(labels_path, 'w') as labels_io, \
        open(images_path, 'w') as images_io, \
        open(uuids_path, 'w') as uuids_io:  # noqa

        for entry in tqdm.tqdm(
            packer.unpack(), total=features_count, desc="Iterating over RCDB entries",
            leave=False,
        ):
            # save images from entry
            image_path = target / entry.label / f"{entry.uuid}.jpeg"

            features_io.write(",".join(map(str, entry.feature)) + "\n")
            labels_io.write(entry.label + "\n")
            uuids_io.write(str(entry.uuid) + "\n")

            images_io.write(str(image_path) + "\n")
            if image_path.exists():
                # check if image can be loaded via pil and whatnot
                continue
            image_path.parent.mkdir(exist_ok=True, parents=True)

            # download image
            download_queue.put((entry.image_url, image_path))
            total_images_to_download += 1
            # ctx.provider.download(url=entry.image_url, destination=image_path)

    progress_bar.total = total_images_to_download
    progress_bar.refresh()
    click.echo(f"Downloading {total_images_to_download} images not present in FS, please wait...")
    download_queue.join()
    progress_bar.close()
    click.echo("Download is complete")


@rcdb.command(name='upload')
@click.argument('rcdb_file', type=click.Path(exists=True, dir_okay=False, file_okay=True))
@click.option('-r', '--retailer-codename', type=click.STRING)
@click.option('-m', '--model-codename', type=click.STRING)
@click.option('-w', '--with-images', is_flag=True)
@pass_rebotics_context
def rcdb_upload(ctx, rcdb_file, **kwargs):
    """
    Upload RCDB file
    """
    # retrieve model_id by the model_codename
    # read features count in the file

    kwargs['archive_size'] = pathlib.Path(rcdb_file).stat().st_size
    packer = VirtualClassificationDatabasePacker(source=str(rcdb_file))
    kwargs['features_count'] = packer.get_features_count()

    ctx.verbose_log(f"Archive size: {kwargs['archive_size']}. "
                    f"Features count: {kwargs['features_count']}")

    ctx.verbose_log("Upload rcdb file using presigned post URL")
    with open(rcdb_file, 'rb') as file_io:
        file_upload = ctx.provider.upload_file(file_io, filename=rcdb_file.name)
    file_id = file_upload['id']

    # call API to create an RCDB entry in database
    ctx.provider.save_rcdb(
        file_id,
        **kwargs
    )


@rcdb.command(name='copy')
@click.argument("backup_id", type=int)
@click.option("-r", "--retailer-codename", type=click.STRING, required=True, help="Retailer codename is required")
@click.option('-m', '--model-codename', type=click.STRING, help="If not specified,"
                                                                " the model_codename from the backup will be used")
@click.option("--admin-role", type=click.STRING, help="Uses the role, if not specified, "
                                                      "will be using the same role from fvm. "
                                                      "E.g. we have r3dev and r3us for both fvm and admin")
@pass_rebotics_context
@pass_context
def rcdb_copy_from_admin(click_ctx, ctx, backup_id, retailer_codename, model_codename, admin_role):
    """Copy CORE rcdb from the admin and upload and assign the rcdb file to appropriate retailer and model.

    To create rcdb backup from CORE go to admin application on /admin/nn_models/retailermodel/
    Click on "Download reference data"
    Wait a couple of minutes, and navigate to /admin/classification_data/featurevectorbackup/
    Retrieve the ID of the backup and use it with this command.
    """
    try:
        if admin_role is None:
            admin_role = ctx.role
            ctx.verbose_log(f"Admin role is not specified, using same role for fvm: {admin_role}")
        admin_config = ReboticsScriptsConfiguration(
            os.path.join(app_dir, 'admin.json'),
            provider_class=AdminProvider
        )
        admin_provider: AdminProvider = admin_config.get_provider(admin_role)

        if admin_provider is None:
            raise Exception(f"There is no admin provider with role name {admin_role}")
    except Exception as exc:
        click.echo(f"Failed to initialize admin provider with {exc}")
        sys.exit(1)

    ctx.verbose_log(f"Fetching rcdb backup {backup_id} from {admin_provider.host}")
    backup = admin_provider.rcdb.get(backup_id)
    ctx.verbose_log("Backup data: ")
    if ctx.verbose:
        ctx.format_result(backup, force_format='json')

    if backup['status'] != 'EXPORT_DONE':
        click.echo(f"The backup #{backup_id} export may not be finished and has status {backup['status']}")

    backup_url = backup['backup']
    rcdb_file_path = pathlib.Path(f"{retailer_codename}_{datetime.now().strftime('%Y_%m_%d_%H-%M')}.rcdb")

    ctx.verbose_log(f"Downloading rcdb backup from {backup_url} to {rcdb_file_path}")

    remote_loaders.download(backup_url, rcdb_file_path, progress_bar=True)

    ctx.verbose_log(f"Invoking rcdb_upload from {rcdb_file_path}")

    selected_model_codename = model_codename
    if model_codename is None:
        ctx.verbose_log('Setting model codename from backup')
        selected_model_codename = backup.get('model_codename')

    if selected_model_codename is None:
        click.echo("There is no specified model_codename.")
        sys.exit(1)

    click_ctx.invoke(rcdb_upload,
                     rcdb_file=rcdb_file_path,
                     retailer_codename=retailer_codename,
                     model_codename=selected_model_codename,
                     with_images=False)
