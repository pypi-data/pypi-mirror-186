#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#

import json
from pathlib import Path

import requests
from requests.exceptions import SSLError
from requests_pkcs12 import post

from aos_signer.service_config.service_configuration import ServiceConfiguration
from aos_signer.signer.common import ca_certificate
from aos_signer.signer.common import print_message
from aos_signer.signer.errors import SignerError
from aos_signer.signer.user_credentials import UserCredentials


def run_upload(config: ServiceConfiguration, config_path: Path):
    uc = UserCredentials(config, config_path)
    uc.find_upload_key_and_cert()

    upload_data = {'service': config.publish.service_uid, 'package_version': 2}
    version = config.publish.version

    if version:
        upload_data['version'] = version

    file_to_upload = (config_path.parent.parent / 'service.tar.gz').resolve()
    print_message("Uploading...                   ", end='')

    with ca_certificate() as server_certificate_path:
        try:
            if uc.pkcs_credentials is None:
                resp = requests.post(
                    'https://{}:10000/api/v1/services/versions/'.format(config.publish.url),
                    files={'file': open(file_to_upload, 'rb')},
                    data=upload_data,
                    cert=(uc.upload_cert_path, uc.upload_key_path),
                    verify=server_certificate_path)
            else:
                resp = post(
                    'https://{}:10000/api/v1/services/versions/'.format(config.publish.url),
                    files={'file': open(file_to_upload, 'rb')},
                    data=upload_data,
                    pkcs12_filename=uc.upload_p12_path,
                    pkcs12_password='',
                    verify=server_certificate_path)
        except SSLError:
            print_message('[yellow]TLS verification against Aos Root CA failed.')
            print_message('[yellow]Try to POST using TLS verification against system CAs.')
            if uc.pkcs_credentials is None:
                resp = requests.post(
                    'https://{}:10000/api/v1/services/versions/'.format(config.publish.url),
                    files={'file': open(file_to_upload, 'rb')},
                    data=upload_data,
                    cert=(uc.upload_cert_path, uc.upload_key_path))
            else:
                resp = post(
                    'https://{}:10000/api/v1/services/versions/'.format(config.publish.url),
                    files={'file': open(file_to_upload, 'rb')},
                    data=upload_data,
                    pkcs12_filename=uc.upload_p12_path,
                    pkcs12_password='')

        if resp.status_code != 201:
            print_message('[red]ERROR')
            print_message('[red]Server returned error while uploading:')
            try:
                errors = json.loads(resp.text)
                message = ''
                for key, value in errors.items():
                    message += f'   {key}: {value}'
                    raise SignerError(message)
            except json.JSONDecodeError:
                raise SignerError(resp.text)

    print_message(f"[green]DONE")
    print_message(f'[green]Service successfully uploaded!')
