#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#

import argparse
import sys
from pathlib import Path

import aos_signer.signer.common
from aos_signer.signer.commands import bootstrap_service_folder, validate_service_config, upload_service, sign_service
from aos_signer.signer.errors import SignerError
from aos_signer.signer.signer import logger

try:
    from importlib.metadata import version, PackageNotFoundError  # noqa: WPS433
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # noqa: WPS433, WPS440

_COMMAND_INIT = 'init'
_COMMAND_SIGN = 'sign'
_COMMAND_UPLOAD = 'upload'
_COMMAND_VALIDATE = 'validate'
_COMMAND_GO = 'go'
DEFAULT_CONFIG_PATH = 'meta/config.yaml'


def _parse_args():
    """User arguments parser.

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog='Aos Signer Tool',
        description='This tool will help you to prepare, sign and upload service to Aos Cloud',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    sub_parser = parser.add_subparsers(title='Commands')

    init = sub_parser.add_parser(
        _COMMAND_INIT,
        help='Generate required folders and configuration file. If you don\'t know where to start type aos-signer init'
    )
    init.set_defaults(func=run_init_signer)

    validate = sub_parser.add_parser(
        _COMMAND_VALIDATE,
        help='Validate config file.'
    )
    validate.set_defaults(func=run_validate)

    sign = sub_parser.add_parser(
        _COMMAND_SIGN,
        help='Sign Service. Read config and create signed archive ready to be uploaded.'
    )
    sign.set_defaults(func=run_sign)

    upload = sub_parser.add_parser(
        _COMMAND_UPLOAD,
        help='Upload Service to the Cloud.'
             'Address, security credentials and service UID is taken from config.yaml in meta folder.'
    )
    upload.set_defaults(func=run_upload_service)

    go = sub_parser.add_parser(
        _COMMAND_GO,
        help='Sign and upload Service to the Cloud.'
             'Address, security credentials and service UID are taken from config.yaml in meta folder.'
    )
    go.set_defaults(func=run_go)

    try:
        parser.add_argument(
            '-V',
            '--version',
            action='version',
            version=f'%(prog)s {version("aos-signer")}',  # noqa: WPS323,WPS237
        )
    except PackageNotFoundError:
        parser.add_argument(
            '-V',
            '--version',
            action='version',
            version=f'%(prog)s',  # noqa: WPS323,WPS237
        )
    return parser


def run_init_signer(args):
    bootstrap_service_folder()


def run_validate(args):
    validate_service_config(Path(DEFAULT_CONFIG_PATH))


def run_upload_service(args):
    upload_service(Path(DEFAULT_CONFIG_PATH))


def run_sign(args):
    sign_service(Path(DEFAULT_CONFIG_PATH), 'src', '.')


def run_go(args):
    config_path = Path(DEFAULT_CONFIG_PATH)
    sign_service(config_path, 'src', '.')
    upload_service(config_path)


def main():
    """Terminal main entry point."""
    parser = _parse_args()
    args = parser.parse_args()
    aos_signer.signer.common.allow_print = True
    try:
        if not hasattr(args, 'func'):
            args.func = run_sign
        args.func(args)
    except SignerError as se:
        aos_signer.signer.common.print_message('[red]Process failed with error: [/red]')
        se.print_message()
        sys.exit(1)
    except Exception as sce:
        aos_signer.signer.common.print_message('[red]Process failed with error: [/red]')
        aos_signer.signer.common.print_message(str(sce))
        logger.exception(sce)
        sys.exit(1)


if __name__ == '__main__':
    main()
