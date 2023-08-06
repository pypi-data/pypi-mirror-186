#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#
import json
import sys
from abc import ABC, abstractmethod

import jsonschema

if sys.version_info > (3, 9):
    from importlib import resources as pkg_resources  # noqa: WPS433, WPS440
else:
    import importlib_resources as pkg_resources  # noqa: WPS433, WPS440


class ConfigChapter(ABC):

    @staticmethod
    @abstractmethod
    def from_yaml(input_dict):
        pass

    @staticmethod
    def validate(received_chapter, validation_schema=None, validation_file=None):
        if validation_schema is not None:
            return jsonschema.validate(received_chapter, schema=validation_schema)

        if validation_file is not None:
            schema = pkg_resources.files('aos_signer') / ('files/' + validation_file)
            with pkg_resources.as_file(schema) as schema_path:
                with open(schema_path, 'r') as f:
                    schema_loaded = json.loads(f.read())
                    return jsonschema.validate(received_chapter, schema=schema_loaded)
