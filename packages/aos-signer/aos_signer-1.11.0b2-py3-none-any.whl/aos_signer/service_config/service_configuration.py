#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#

import json
import os
import sys

import jsonschema
import ruamel.yaml

if sys.version_info > (3, 9):
    from importlib import resources as pkg_resources  # noqa: WPS433, WPS440
else:
    import importlib_resources as pkg_resources  # noqa: WPS433, WPS440

from aos_signer.signer.errors import SignerConfigError
from .models.build import Build
from .models.configuration import Configuration
from .models.publish import Publish
from .models.publisher import Publisher
from ..signer.common import print_message

CONFIG_NOT_FOUND_HELP = [
    "if you have configured service, run aos-signer tool from the parent directory of 'meta' dir",
    "If you are configuring service for the first time, run 'aos-signer init' first"
]


class ServiceConfiguration(object):

    DEFAULT_META_FOLDER = 'meta'
    DEFAULT_CONFIG_FILE_NAME = 'config.yaml'

    def __init__(self, file_path=None):
        self._config_path = file_path

        if file_path is None:
            file_path = os.path.join(self.DEFAULT_META_FOLDER, self.DEFAULT_CONFIG_FILE_NAME)

        if not os.path.isfile(file_path):
            raise SignerConfigError(f"Config file {file_path} not found. Exiting...", CONFIG_NOT_FOUND_HELP)

        yaml = ruamel.yaml.YAML()
        print_message("[bright_black]Starting CONFIG VALIDATION process...")
        print_message("Validating config...           ", end='')

        with open(file_path, 'r') as file:
            try:
                schema = pkg_resources.files('aos_signer') / 'files/root_schema.json'
                loaded = yaml.load(file)
                with pkg_resources.as_file(schema) as schema_path:
                    with open(schema_path, 'r') as f:
                        sc = json.loads(f.read())
                        jsonschema.validate(loaded, schema=sc)
                self._publisher = Publisher.from_yaml(loaded.get('publisher'))
                self._publish = Publish.from_yaml(loaded.get('publish'))
                self._build = Build.from_yaml(loaded.get('build'))
                self._configuration = Configuration.from_yaml(loaded.get('configuration'))
                print_message(f"[green]VALID")
            except (ruamel.yaml.parser.ParserError,
                    ruamel.yaml.scanner.ScannerError,
                    jsonschema.exceptions.ValidationError) as exc:
                print_message(f"[red]ERROR")
                raise SignerConfigError(str(exc))

    @property
    def publisher(self):
        return self._publisher

    @property
    def publish(self):
        return self._publish

    @property
    def build(self):
        return self._build

    @property
    def configuration(self):
        return self._configuration

    @property
    def config_path(self):
        return self._config_path
