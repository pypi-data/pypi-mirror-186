#
#  Copyright (c) 2018-2019 Renesas Inc.
#  Copyright (c) 2018-2019 EPAM Systems Inc.
#
import base64
import glob
import jwt
import logging
import os
import shutil
from distutils.dir_util import copy_tree
from multiprocessing import cpu_count
from pathlib import Path
from tempfile import TemporaryDirectory

from aos_signer.service_config.service_configuration import ServiceConfiguration
from aos_signer.signer.common import print_message
from aos_signer.signer.errors import SignerError
from aos_signer.signer.file_details import FileDetails
from .user_credentials import UserCredentials

logger = logging.getLogger(__name__)


class Signer:
    _SERVICE_FOLDER = 'service'
    _DEFAULT_STATE_NAME = 'default_state.dat'
    _THREADS = cpu_count()
    _SERVICE_FILE_ARCHIVE_NAME = 'service'

    def __init__(self, src_folder, package_folder, config: ServiceConfiguration, config_path: Path):
        self._config = config
        self._src = src_folder
        self._package_folder = package_folder
        self._config_path = config_path

    def process(self):
        with TemporaryDirectory() as tmp_folder:
            self._copy_application(folder=tmp_folder)
            self._copy_yaml_conf(folder=tmp_folder)
            self._copy_state(folder=tmp_folder)
            self._validate_source_folder(folder=tmp_folder)
            file_name = self._compose_archive(folder=tmp_folder)
            self._sign_file(folder=tmp_folder, file=file_name)
            package_name = self._compose_package(folder=tmp_folder)
            print_message(f'[green]Service package created: {package_name}')

    def _sign_file(self, folder, file):
        print_message('Sing package...       ', end='')
        service_file_details = self._calculate_file_hash(file, folder)
        config_file_details = self._calculate_file_hash(Path(folder) / 'config.yaml', folder)
        uc = UserCredentials(self._config, self._config_path)
        uc.find_sign_key_and_cert()
        payload = [
            {
                'name': os.path.basename(service_file_details.name),
                'hash': service_file_details.hash,
                'size': service_file_details.size,
            },
            {
                'name': os.path.basename(config_file_details.name),
                'hash': config_file_details.hash,
                'size': config_file_details.size,
            },
        ]
        issuer = uc.get_issuer(uc.sign_certificate)
        serial_number = uc.get_certificate_serial_number_hex(uc.sign_certificate)
        kid = base64.b64encode((issuer + ':' + serial_number).encode()).decode()
        sig = jwt.encode(
            {'data': payload}, uc.sign_key, algorithm='RS256', headers={'kid': kid}
        )
        with open(Path(folder) / 'package.sign', 'w') as fp:
            fp.write(sig)
        print_message('[green]DONE')

    def _copy_state(self, folder):
        state_info = self. _config.configuration.state
        print_message('Copying default state...       ', end='')

        if not state_info:
            print_message('[yellow]SKIP')
            return

        if not state_info.get('required', False):
            print_message('[yellow]Not required by config')
            return

        state_filename = state_info.get('filename', 'state.dat')
        if state_filename:
            try:
                shutil.copy(
                    os.path.join('meta', state_filename),
                    os.path.join(folder, self._DEFAULT_STATE_NAME)
                )
                print_message('[green]DONE')
            except FileNotFoundError:
                print_message('[red]ERROR')
                raise SignerError(f'State file "{state_filename}" defined in the configuration does not exist.')

    def _copy_application(self, folder):
        print_message('Copying application...         ', end='')
        temp_service_folder = Path(folder) / self._SERVICE_FOLDER
        temp_service_folder.mkdir(parents=True, exist_ok=True)
        copy_tree(self._src, str(temp_service_folder), preserve_symlinks=True)
        print_message('[green]DONE')

    def _copy_yaml_conf(self, folder):
        print_message('Copying configuration...       ', end='')
        shutil.copyfile(self._config.config_path, os.path.join(folder, 'config.yaml'))
        print_message('[green]DONE')

    def _calculate_file_hash(self, file_name, tmp_folder):
        file_details = FileDetails(root=tmp_folder, file=file_name)
        file_details.calculate()
        return file_details

    def _validate_source_folder(self, folder):
        src_len = len([item for item in folder.split(os.path.sep) if item])
        regular_files_only = True
        for root, dirs, files in os.walk(folder):
            splitted_root = [item for item in root.split(os.path.sep) if item][src_len:]
            if splitted_root:
                root = os.path.join(*splitted_root)
            else:
                root = ''

            # Check for links in directories
            for dir_name in dirs:
                full_dir_name = os.path.join(folder, root, dir_name)
                if os.path.islink(full_dir_name):
                    if self._config.build.symlinks == 'delete':
                        logger.info('Removing non-regular directory "{}"'.format(os.path.join(root, dir_name)))
                        os.remove(full_dir_name)
                    elif self._config.build.symlinks == 'raise':
                        logger.error('This is not a regular directory "{}".'.format(os.path.join(root, dir_name)))
                        regular_files_only = False

            # Process files
            for file_name in files:
                full_file_name = os.path.join(folder, root, file_name)

                if os.path.islink(full_file_name):
                    if self._config.build.symlinks == 'delete':
                        logger.info('Removing non-regular file "{}"'.format(os.path.join(root, file_name)))
                        os.remove(full_file_name)
                    elif self._config.build.symlinks == 'raise':
                        logger.error('This is not a regular file "{}".'.format(os.path.join(root, file_name)))
                        regular_files_only = False
                    continue

        if not regular_files_only:
            raise SignerError('Source code folder contains non regular file(s).')

    def _compose_archive(self, folder):
        print_message('Creating archive...            ', end='')
        scr_service_files = glob.glob(folder + '/*')
        arch = shutil.make_archive(os.path.join(folder, self._SERVICE_FILE_ARCHIVE_NAME), 'gztar', folder)
        for f in scr_service_files:
            if Path(f) == (Path(folder) / 'config.yaml'):
                continue
            if os.path.isfile(f):
                os.unlink(f)
            else:
                shutil.rmtree(f)
        print_message('[green]DONE')
        return arch

    def _compose_package(self, folder):
        print_message('Creating service package...            ', end='')
        arch = shutil.make_archive(os.path.join(self._package_folder, self._SERVICE_FILE_ARCHIVE_NAME), 'gztar', folder)
        print_message('[green]DONE')
        return arch


def _test_function(_unused=None):
    return 0
