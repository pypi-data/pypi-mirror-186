#
#  Copyright (c) 2018-2022 Renesas Inc.
#  Copyright (c) 2018-2022 EPAM Systems Inc.
#
import sys
from pathlib import Path

from aos_signer.service_config.service_configuration import ServiceConfiguration
from aos_signer.signer.bootstrapper import run_bootstrap
from aos_signer.signer.common import print_message
from aos_signer.signer.errors import SignerError
from aos_signer.signer.signer import Signer
from aos_signer.signer.uploader import run_upload


def bootstrap_service_folder():
    """Create service folder structure and config.yaml."""
    print_message("[green]Starting INIT process...")
    run_bootstrap()


def validate_service_config(config_path: Path):
    """Validate config.yaml.
    Args:
        config_path: Path to config file.
    Raises:
        SignerConfigError: If config is not valid.
    """
    print_message("[bright_black]Starting CONFIG VALIDATION process...")
    ServiceConfiguration(Path(config_path))
    print_message("[green]Config is valid")


def upload_service(config_path: Path):
    """Upload service.
    Args:
        config_path: Path to config file.
    Raises:
        SignerError: If upload failed.
    """
    config = ServiceConfiguration(config_path)

    print_message("[bright_black]Starting SERVICE UPLOAD process...")
    try:
        run_upload(config, Path(config_path))
    except OSError:
        raise SignerError(str(sys.exc_info()[1]))


def sign_service(config_path: Path, sources_folder: str = 'src', package_folder: str = '.'):
    """Sign service.
    Args:
        config_path: Path to config file.
        sources_folder: Service sources folder.
        package_folder: Result save folder.
    Raises:
        SignerError: If sign process failed.
    """
    print_message("[bright_black]Starting SERVICE SIGNING process...")
    config = ServiceConfiguration(config_path)
    try:
        s = Signer(
            src_folder=sources_folder,
            package_folder=package_folder,
            config=config,
            config_path=Path(config_path)
        )
        s.process()
    except OSError:
        raise SignerError(str(sys.exc_info()[1]))
