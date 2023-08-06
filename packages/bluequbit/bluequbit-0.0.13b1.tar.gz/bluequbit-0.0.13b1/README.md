![lint status](https://github.com/BlueQubitDev/deqart-python-sdk/actions/workflows/lint.yml/badge.svg) ![release status](https://github.com/BlueQubitDev/deqart-python-sdk/actions/workflows/release.yml/badge.svg) ![tests status](https://github.com/BlueQubitDev/deqart-python-sdk/actions/workflows/tests.yml/badge.svg) ![docs status](https://github.com/BlueQubitDev/deqart-python-sdk/actions/workflows/deploy_docs.yml/badge.svg)


# Deqart Python SDK

## Usage

### Interface with the Deqart server

#### Initialization

```python
import deqart

# If you have run the line below once, subsequent initialization no longer
# requires explicit API token, i.e. deqart.init() without an argument is
# sufficient. This is because the token is automatically saved to
# ~/.config/deqart/config.json.
dq = deqart.init(YOUR_API_TOKEN)
```

#### Estimating how long it takes to simulate a circuit

```python
import qiskit

import deqart

dq = deqart.init()

qc = qiskit.QuantumCircuit(2)
qc.h(0)
qc.x(1)

result = dq.estimate_job_runtime(qc)
print(result)
# Output
# {
#   'device': 'qsim_simulator',
#   'estimate_ms': 100,
#   'num_qubits': 2,
#   'qc': 'UUlTS0lUBQAVAgAAAAAAAAABcQAKaQAIAAAAAgAAAAAAAAAAAAAABAAAAAEAAAAAAAAAAmNpcmN1aXQtNzgAAAAAAAAAAG51bGxxAQAAAAIAAQFxAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAUAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASEdhdGVxAAAAAAAFAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhHYXRlcQAAAAEAAA==',
#   'warning_message': 'This is just an estimate; the actual runtime may be less or more.'
# }
```

#### Submitting a simulation job and retrieving it

```
import deqart

dq = deqart.init()

dq.submit_job(qc)
result = dq.search_jobs()
print(result)
# Output
# {
#   'column_names': ['job_id', 'run_status', 'success', 'worker_runtime_ms', 'created_on'],
#   'data': [['4j2u9lb031YgfPpB', 'QUEUED', None, None, '2022-10-20T07:10:20.316Z']], 'total_count': 1
# }
```

### Circuit serialization

You can decode a quantum circuit of Braket/Cirq/Qiskit to/from JSON string.

```python
import deqart.circuit_serialization as circuit_serialization

# Example with Cirq circuit
encoded_cirq = circuit_serialization.encode_circuit(qc_cirq)
decoded_cirq = circuit_serialization.decode_circuit(encoded_cirq)
```
