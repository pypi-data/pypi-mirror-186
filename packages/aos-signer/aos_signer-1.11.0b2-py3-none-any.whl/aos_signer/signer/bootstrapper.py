#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#

import os
import sys

from aos_signer.signer.common import FILES_DIR, print_message
from aos_signer.signer.errors import NoAccessError

if sys.version_info > (3, 9):
    from importlib import resources as pkg_resources  # noqa: WPS433, WPS440
else:
    import importlib_resources as pkg_resources  # noqa: WPS433, WPS440

_meta_folder_name = 'meta'
_src_folder_name = 'src'
_config_file_name = 'config.yaml'


def run_bootstrap():
    _create_folder_if_not_exist(_meta_folder_name)
    _create_folder_if_not_exist(_src_folder_name)
    _init_conf_file()
    print_message('[green]DONE[/green]')
    _print_epilog()


def _create_folder_if_not_exist(folder_name):
    try:
        if os.path.isdir(folder_name):
            print_message(f'Directory [cyan]\[{folder_name}][/cyan] exists... [yellow]Skipping[/yellow]') # noqa: WPA605
        else:
            os.mkdir(folder_name)
            print_message(f'Directory [cyan]\[{folder_name}][/cyan] created.')  # noqa: WPA605
    except PermissionError:
        raise NoAccessError


def _init_conf_file():
    conf_file_path = os.path.join(_meta_folder_name, _config_file_name)
    if os.path.isfile(conf_file_path):
        print_message(f'Configuration file [cyan]{_config_file_name}[/cyan] exists... [yellow]Skipping[/yellow]')
    else:
        with open(conf_file_path, 'x') as cfp:
            config = pkg_resources.files(FILES_DIR) / f'files/{_config_file_name}'
            with pkg_resources.as_file(config) as config_path:
                cfp.write(config_path.read_text())
        print_message(f'Config file  [cyan]{_meta_folder_name}/{_config_file_name}[/cyan] created')


def _print_epilog():
    print_message('---------------------------')
    print_message('[dim]Further steps:')
    print_message(f'Copy your service files with desired folders to [cyan]\[src][/cyan] folder.')
    print_message('Update [cyan]meta/config.yaml[/cyan] with desired values.')
    print_message('Run [bright blue]aos-signer sign[/] to sign service and'
                  " '[bright blue]aos-signer upload[/]' to upload signed service to the cloud.")
