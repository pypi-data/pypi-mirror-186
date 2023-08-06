# Mypy; for the `|` operator purpose
# Remove this __future__ import once the oldest supported Python is 3.10
from __future__ import annotations

import logging
import os
from pathlib import Path

import packaging.version

from . import exceptions
from .bluequbit_client import BQClient
from .estimate_result import EstimateResult
from .http_adapter import HTTP_SESSION_WITH_TIMEOUT_AND_RETRY
from .job_result import JobResult
from .version import __version__

formatter = logging.Formatter(fmt="BQ-PYTHON-SDK - %(levelname)s - %(message)s")
# formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("bluequbit-python-sdk")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def _check_version():
    local_version = packaging.version.parse(__version__)
    if local_version.is_prerelease:
        logger.warning(
            "Development version %s of BQ Python SDK is being used", __version__
        )
    req = HTTP_SESSION_WITH_TIMEOUT_AND_RETRY.get(
        "https://pypi.python.org/pypi/bluequbit/json", timeout=2.0
    )
    if not req.ok:
        return

    # find max version on PyPI
    releases = req.json().get("releases", [])
    pip_version = packaging.version.parse("0")
    for release in releases:
        ver = packaging.version.parse(release)
        if not ver.is_prerelease or local_version.is_prerelease:
            pip_version = max(pip_version, ver)

    if pip_version.major > local_version.major:
        logger.warning(
            "There is a major upgrade of BlueQubit Python SDK available on PyPI. We recommend upgrading. Run 'pip install --upgrade bluequbit' to upgrade from your version %s to %s.",
            local_version,
            pip_version,
        )
    elif pip_version > local_version:
        logger.info(
            "There is a newer version of BlueQubit Python SDK available on PyPI. Run 'pip install --upgrade bluequbit' to upgrade from your version %s to %s.",
            local_version,
            pip_version,
        )


def init(
    api_token: str | None = None,
    path_to_config_json: str | Path | None = None,
    check_for_latest_version: bool = True,
) -> BQClient:
    """Initializes and authenticates to BlueQubit platform using the config file.
    If not initialized then $HOME/.config/bluequbit/config.json
    will be used.

    :param api_token: The API token
    :type api_token: str | None

    :param path_to_config_json: Location to config JSON file
    :type path_to_config_json: str | Path | None

    :param check_for_latest_version: Check for the latest version of bluequbit package on PiPy
    :type check_for_latest_version: bool

    :return: BQ client
    :rtype: BQClient
    """
    if check_for_latest_version and os.environ.get("BLUEQUBIT_TESTING") is None:
        try:
            _check_version()
        except:
            pass
    return BQClient(api_token, path_to_config_json)
