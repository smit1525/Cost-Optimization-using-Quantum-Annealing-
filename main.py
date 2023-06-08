import dimod
from dwave.system import DWaveSampler, EmbeddingComposite

# Define the cost optimization problem
def cost_optimization():
    # Create a binary quadratic model (BQM) object
    bqm = dimod.BinaryQuadraticModel.empty(dimod.BINARY)

    # Define the variables
    x = ['x0', 'x1', 'x2', 'x3']

    # Set the objective function coefficients
    bqm.set_linear('x0', 2)
    bqm.set_linear('x1', 3)
    bqm.set_linear('x2', 5)
    bqm.set_linear('x3', 4)

    # Set the quadratic coefficients
    bqm.set_quadratic('x0', 'x1', 1)
    bqm.set_quadratic('x0', 'x2', 3)
    bqm.set_quadratic('x1', 'x2', -2)
    bqm.set_quadratic('x2', 'x3', 1)

    return bqm

# Solve the problem using quantum annealing
sampler = EmbeddingComposite(DWaveSampler())
bqm = cost_optimization()
response = sampler.sample(bqm, num_reads=100)

# Print the solutions and energies
for sample, energy in response.data(['sample', 'energy']):
    print(sample, energy)
