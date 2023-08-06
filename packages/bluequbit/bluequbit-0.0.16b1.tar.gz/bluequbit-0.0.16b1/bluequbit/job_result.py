import datetime
from io import BytesIO

import numpy as np
from dateutil.parser import parse

from .exceptions import BQStatevectorTooLarge
from .http_adapter import HTTP_SESSION_WITH_TIMEOUT_AND_RETRY


class JobResult:
    """This class contains information from a job run on quantum hardware or
    quantum simulators. Mainly it contains the resulting statevector from the
    run. It might contain only partial information, such as job ID,
    when :func:`BQClient.run` is called with ``asynchronous=True``."""

    def __init__(self, data):
        #: str: job id
        self.job_id = data.get("job_id")

        #: str: job run status, can be one of ``"FAILED_VALIDATION"`` | ``"PENDING"`` | ``"QUEUED"`` | ``"RUNNING"`` | ``"TERMINATED"`` | ``"CANCELED"`` | ``"NOT_ENOUGH_FUNDS"`` | ``"COMPLETED"``
        self.run_status = data.get("run_status")

        #: str: job name
        self.job_name = data.get("job_name")

        #: int: estimated runtime in milliseconds
        self.estimate_ms = data.get("estimated_runtime_ms")

        #: float: estimated cost in US dollars
        self.estimate_cost = data.get("estimated_cost")
        if self.estimate_cost is not None:
            self.estimate_cost /= 100.0

        #: datetime: job creation date in UTC timezone
        self.created_on = data.get("created_on")
        if self.created_on is not None:
            self.created_on = parse(self.created_on)

        self._results_path = data.get("results_path")
        self.top_100_results = data.get("top_100_results")

        #: int: number of qubits
        self.num_qubits = data.get("num_qubits")
        self.tags = data.get("tags")

        #: datetime: job enqueue time in UTC timezone
        self.queue_start = data.get("queue_start")
        if self.queue_start is not None:
            self.queue_start = parse(self.queue_start)

        #: datetime: job run start time in UTC timezone
        self.run_start = data.get("run_start")
        if self.run_start is not None:
            self.run_start = parse(self.run_start)

        #: datetime: job run end time in UTC timezone
        self.run_end = data.get("run_end")
        if self.run_end is not None:
            self.run_end = parse(self.run_end)

        #: int: time spent in queue in milliseconds
        self.queue_time_ms = None
        if self.queue_start is not None and self.run_start is not None:
            self.queue_time_ms = int(
                (self.run_start - self.queue_start) / datetime.timedelta(milliseconds=1)
            )

        #: int: job runtime in milliseconds
        self.run_time_ms = None
        if self.run_start is not None and self.run_end is not None:
            self.run_time_ms = round(
                (self.run_end - self.run_start) / datetime.timedelta(milliseconds=1)
            )

        #: str: error message if failed
        self.error_message = data.get("error_message")

        #: float: job cost in US dollars
        self.cost = data.get("cost")
        if self.cost is not None:
            self.cost /= 100.0
        self._metadata = None
        self._statevector = None

    def get_statevector(self) -> np.array:
        """Return statevector of the job. If the statevector is too large then throws exception.

        :rtype: NumPy array
        """

        if self._statevector is None:
            response = HTTP_SESSION_WITH_TIMEOUT_AND_RETRY.get(
                self._results_path + "statevector.txt"
            )
            if response.ok:
                data = response.content
                self._statevector = np.loadtxt(BytesIO(data), dtype=np.complex_)
        if not self._statevector is None:
            return self._statevector
        else:
            raise BQStatevectorTooLarge(self.num_qubits)

    def get_counts(self) -> dict:
        if self._metadata is None:
            response = HTTP_SESSION_WITH_TIMEOUT_AND_RETRY.get(
                self._results_path + "metadata.json"
            )
            self._metadata = response.json()
        if "counts" not in self._metadata:
            raise RuntimeError("The job result metadata doesn't contain counts.")
        return self._metadata["counts"]

    @property
    def ok(self) -> bool:
        """``True``, if job's current run status is ``"COMPLETED"``,
        else ``False``."""

        return self.run_status == "COMPLETED"

    def __str__(self):
        repr = f"Job ID: {self.job_id}"
        if self.job_name is not None:
            repr += f", name: {self.job_name}"
        repr += f", run status: {self.run_status}, created on: {self.created_on}"
        if (
            self.run_status in ["PENDING", "QUEUED", "RUNNING"]
            and self.estimate_ms is not None
        ):
            repr += f", estimated runtime: {self.estimate_ms} ms"
            repr += f", estimated cost: ${self.estimate_cost:.2f}"
        if self.queue_time_ms is not None:
            repr += f", queue time: {self.queue_time_ms} ms"
        if self.run_time_ms is not None:
            repr += f", run time: {self.run_time_ms} ms"
        if self.cost is not None:
            repr += f", cost: ${self.cost:.2f}"
        if self.num_qubits is not None:
            repr += f", num qubits: {self.num_qubits}"
        if self.error_message is not None:
            repr += f", error_message: {self.error_message}"
        return repr
