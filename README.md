# Cost optimization using Quantum Annealing

In this example, we define a cost optimization problem using a binary quadratic model (BQM). The objective function and constraints are defined in the cost_optimization function. The variables (x0, x1, x2, x3) are created, and their corresponding linear and quadratic coefficients are set in the BQM.

We then use DWaveSampler() and EmbeddingComposite() to solve the problem through quantum annealing on the D-Wave quantum computer. The sample method is called on the sampler object, passing in the BQM and the desired number of reads.

Finally, we iterate through the results and print the solutions (sample) and energies. The solutions represent the optimized values of the variables that minimize the cost function.

Make sure to have the D-Wave Ocean SDK installed and access to a D-Wave quantum computer or system to run this code on actual quantum hardware.
