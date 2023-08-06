# Mypy; for the `|` operator purpose
# Remove this __future__ import once the oldest supported Python is 3.10
from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Any

import packaging.version

from .api import jobs
from .backend_connection import BackendConnection
from .estimate_result import EstimateResult
from .http_adapter import HTTP_SESSION_WITH_TIMEOUT_AND_RETRY
from .job_result import JobResult
from .version import __version__


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


if TYPE_CHECKING:
    import datetime
    from pathlib import Path

# TODO this requires imports of actual quantum libraries for proper type
# checking.
CircuitT = Any

logger = logging.getLogger("bluequbit-python-sdk")


class BQClient:
    """Client for managing jobs on BQ platform.

    :param api_token: API token of the user
    """

    def __init__(self, api_token: str | None = None):
        if os.environ.get("BLUEQUBIT_TESTING") is None:
            try:
                _check_version()
            except:
                pass
        self._backend_connection = BackendConnection(api_token)

    def estimate(
        self,
        circuit: CircuitT,
    ) -> EstimateResult:
        """Estimate job runtime

        :param circuit: Quantum circuit
        :type circuit: Cirq, Qiskit, circuit
        :return: Estimate result class
        :rtype: EstimateResult
        """
        return EstimateResult(
            jobs.estimate_job_runtime(self._backend_connection, circuit)
        )

    def run(
        self,
        circuit: CircuitT,
        asynchronous: bool = False,
        job_name: str | None = None,
    ) -> JobResult:
        """Run job on BQ Platform

        :param circuit: Quantum circuit
        :type circuit: Cirq, Qiskit, circuit
        :param asynchronous: if set to False, wait for job completion before returning. If set to True, return immediately
        :type asynchronous: bool
        :param job_name: customizable job name
        :type job_name: str
        :return: JobResult metadata
        :rtype: JobResult
        """
        submitted_job = JobResult(
            jobs.submit_job(self._backend_connection, circuit, job_name)
        )
        if submitted_job.run_status == "FAILED_VALIDATION":
            logger.error(submitted_job)
        else:
            logger.info(f"Submitted {submitted_job}")
            if not asynchronous:
                return self.wait(submitted_job.job_id)
        return submitted_job

    def wait(self, job_id: str) -> JobResult:
        """Wait for job completion

        :param job_id: job_id that can be found as property of JobResult metadata
        :type job_id: str
        :return: JobResult metadata
        :rtype: JobResult
        """
        return JobResult(jobs.wait_for_job(self._backend_connection, job_id))

    def get(self, job_id: str) -> JobResult:
        """Get job current metadata and result

        :param job_id: job ID
        :type job_id: str

        :return: Result of job
        :rtype: JobResult
        """
        job_result = jobs.get(self._backend_connection, job_id)
        jr = JobResult(job_result)
        # logger.info(jr)
        return jr

    def cancel(
        self,
        job_id: str,
        asynchronous: bool = False,
    ) -> JobResult:
        """Cancel job

        :param job_id: job_id that can be found as property of JobResult metadata
        :type job_id: str
        :param asynchronous: if set to False, wait for job completion before returning. If set to True, return immediately
        :type asynchronous: bool
        :return: JobResult metadata
        :rtype: JobResult
        """
        jobs.cancel_job(self._backend_connection, job_id)
        if not asynchronous:
            return self.wait(job_id)
        else:
            return JobResult({"job_id": job_id})

    def search(
        self,
        run_status: str | None = None,
        created_later_than: str | datetime.datetime | None = None,
    ) -> list[JobResult]:
        """Search for jobs of the user

        :param run_status: if not None, run status of jobs to filter, can be one of "FAILED_VALIDATION" | "PENDING" | "QUEUED" | "RUNNING" | "TERMINATED" | "CANCELED" | "NOT_ENOUGH_FUNDS" | "COMPLETED"
        :type run_status: str

        :param created_later_than: if not None, filter by latest datetime. Please add timezone for clarity, otherwise UTC will be assumed
        :type created_later_than: str or datetime.datetime

        :return: Metadata of jobs
        :rtype: list of JobResult
        """
        job_results = jobs.search_jobs(
            self._backend_connection, run_status, created_later_than
        )
        return [JobResult(r) for r in job_results["data"]]
