from jsonschema import ValidationError

from .config_chapter import ConfigChapter


class Build(ConfigChapter):

    def __init__(self, os, arch, sign_key, sign_certificate, sign_pkcs12, remove_non_regular_files, context, symlinks):
        self._os = os
        self._arch = arch
        self._sign_key = sign_key
        self._sign_certificate = sign_certificate
        self._remove_non_regular_files = remove_non_regular_files
        self._context = context
        self._symlinks = symlinks
        self._sign_pkcs12 = sign_pkcs12

    @staticmethod
    def from_yaml(input_dict):
        p = Build(
            os=input_dict.get('os'),
            arch=input_dict.get('arch'),
            sign_key=input_dict.get('sign_key'),
            sign_certificate=input_dict.get('sign_certificate'),
            sign_pkcs12=input_dict.get('sign_pkcs12'),
            remove_non_regular_files=input_dict.get('remove_non_regular_files'),
            context=input_dict.get('context'),
            symlinks=input_dict.get('symlinks', 'copy'),
        )
        ConfigChapter.validate(input_dict, validation_file='build_schema.json')

        if not p.sign_pkcs12 and (not p.sign_key or not p.sign_certificate):
            raise ValidationError('Sign certificate should be specified with sign_pkcs12 entry, '
                                  'or with sign_key and sign_certificate values.')

        return p

    @property
    def os(self):
        return self._os

    @property
    def arch(self):
        return self._arch

    @property
    def sign_key(self):
        return self._sign_key

    @property
    def sign_certificate(self):
        return self._sign_certificate

    @property
    def sign_pkcs12(self):
        return self._sign_pkcs12

    @property
    def remove_non_regular_files(self) -> bool:
        return self._remove_non_regular_files

    @property
    def symlinks(self) -> bool:
        return self._symlinks

    @property
    def context(self):
        return self._context
