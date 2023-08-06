from .config_chapter import ConfigChapter


class Publisher(ConfigChapter):
    def __init__(self, author, company):
        self._author = author
        self._company = company

    @staticmethod
    def from_yaml(input_dict):
        if input_dict is None:
            return Publisher(None, None)

        p = Publisher(input_dict.get('author'), input_dict.get('company'))
        ConfigChapter.validate(input_dict, validation_file='publisher_schema.json')
        return p
