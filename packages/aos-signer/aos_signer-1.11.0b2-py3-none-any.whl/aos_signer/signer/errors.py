#
#  Copyright (c) 2018-2019 Renesas Inc.
#  Copyright (c) 2018-2019 EPAM Systems Inc.
#

from typing import Iterable

from aos_signer.signer.common import console


def print_help_with_spaces(text):
    console.print(f'  {text}')


class SignerError(Exception):
    def __init__(self, message, help_text=None):
        super().__init__(message)
        self.help_text = help_text

    def print_message(self):
        console.print(f'ERROR: {self}', style='red')

        if not self.help_text:
            return

        if not isinstance(self.help_text, Iterable):
            print_help_with_spaces(self.help_text)

        for row in self.help_text:
            print_help_with_spaces(row)


class SignerConfigError(SignerError):
    def __init__(self, message, help_text=None):
        super().__init__(message)
        self.help_text = help_text


class NoAccessError(SignerError):
    def __init__(self, message, help_text=None):
        super().__init__(message)
        self.help_text = help_text
