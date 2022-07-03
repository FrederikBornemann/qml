from dwave.system import DWaveSampler
import dwave.inspector

# Get solver
sampler = DWaveSampler(solver=dict(qpu=True))

# Define a problem (actual qubits depend on the selected QPU's working graph)
h = {}
J = {(0, 4): 1, (0, 5): 1, (1, 4): 1, (1, 5): -1}
all(edge in sampler.edgelist for edge in J)
True
# Sample
response = sampler.sample_ising(h, J, num_reads=100)

# Inspect
dwave.inspector.show(response)