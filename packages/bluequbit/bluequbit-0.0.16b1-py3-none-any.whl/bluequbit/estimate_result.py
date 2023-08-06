class EstimateResult:
    """This class contains information about the estimated runtime/cost that
    will be incurred from running the given circuit on the given quantum
    machine/simulator. `WARNING:` this is just an estimate, the actual runtime/cost
    may be less or more."""

    def __init__(self, data):
        self.device = data.get("device")

        #: int: estimated runtime in milliseconds
        self.estimate_ms = data.get("estimate_ms")

        #: float: estimated cost in US dollars
        self.estimate_cost = data.get("estimated_cost")
        if self.estimate_cost is not None:
            self.estimate_cost /= 100.0

        #: int: number of qubits
        self.num_qubits = data.get("num_qubits")

        #: str: warning message
        self.warning_message = data.get("warning_message")

        #: str: error message if available
        self.error_message = data.get("error_message")

    def __str__(self):
        if self.error_message is not None:
            return f"Estimation failed due to error: {self.error_message}."
        return f"Estimated: runtime: {self.estimate_ms} ms, cost: ${self.estimate_cost:.2f}. {self.warning_message}"
