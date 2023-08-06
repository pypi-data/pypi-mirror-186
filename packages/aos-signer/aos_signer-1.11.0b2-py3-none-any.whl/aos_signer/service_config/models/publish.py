from jsonschema import ValidationError

from .config_chapter import ConfigChapter


class Publish(ConfigChapter):

    def __init__(self, url, service_uid, tls_key, tls_certificate, tls_pkcs12, version):
        self._url = url
        self._service_uid = service_uid
        self._tls_key = tls_key
        self._tls_certificate = tls_certificate
        self._tls_pkcs12 = tls_pkcs12
        self._version = version

    @staticmethod
    def from_yaml(input_dict):
        p = Publish(
            input_dict.get('url'),
            input_dict.get('service_uid'),
            input_dict.get('tls_key'),
            input_dict.get('tls_certificate'),
            input_dict.get('tls_pkcs12'),
            input_dict.get('version'),
        )
        ConfigChapter.validate(input_dict, validation_file='publish_schema.json')

        if not p.tls_pkcs12 and (not p.tls_key or not p.tls_certificate):
            raise ValidationError('TLS certificate should be specified with tls_pkcs12 entry, '
                                  'or with tls_key and tls_certificate values.')
        return p

    @property
    def url(self):
        return self._url

    @property
    def service_uid(self):
        return self._service_uid

    @property
    def tls_key(self):
        return self._tls_key

    @property
    def tls_certificate(self):
        return self._tls_certificate

    @property
    def tls_pkcs12(self):
        return self._tls_pkcs12

    @property
    def version(self):
        return self._version
