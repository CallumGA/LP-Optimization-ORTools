'''
    Linear programming problem solved via OR tools mathopt solver - solved with simplex algorithm.

    Includes no upper or lower bounds for variables, but includes multiple linear constraints.

    Problem:
    Maximize:     3x + 4y

    Subject to:   x + 2y ≤ 14
                  3x - y ≥ 0
                  x - y ≤ 2
'''

from ortools.math_opt.python import mathopt

model = mathopt.Model(name="LP-example")

x = model.add_variable(name='x')
y = model.add_variable(name='y')

model.add_linear_constraint(x + 2 * y <= 14)
model.add_linear_constraint(3 * x - y >= 0)
model.add_linear_constraint(x - y <= 2)

model.maximize_linear_objective(3*x + 4*y)

solver = mathopt.solve(model, mathopt.SolverType.GLOP)

if solver.termination.reason != mathopt.TerminationReason.OPTIMAL:
    raise RuntimeError("Solver did not find optimal solution.")

print("Optimal Objective value:", round(solver.objective_value()))
print("x =", round(solver.variable_values()[x]))
print("y =", round(solver.variable_values()[y]))

'''
Output: 
MathOpt solve succeeded
Optimal Objective value: 34
x: 6
y: 4

Explanation: 
This time we have no upper or lower bounds on x or y, just linear constraints. 
Optimal objective value of the function as it is maximized is 34, where x is 6 and y is 4.

'''