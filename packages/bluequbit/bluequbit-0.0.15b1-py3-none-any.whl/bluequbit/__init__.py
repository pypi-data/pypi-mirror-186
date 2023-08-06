# Mypy; for the `|` operator purpose
# Remove this __future__ import once the oldest supported Python is 3.10
import logging

from . import exceptions
from .bluequbit_client import BQClient
from .estimate_result import EstimateResult
from .job_result import JobResult
from .version import __version__

formatter = logging.Formatter(fmt="BQ-PYTHON-SDK - %(levelname)s - %(message)s")
# formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("bluequbit-python-sdk")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
