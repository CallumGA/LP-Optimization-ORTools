'''
    Linear programming problem solved via OR tools mathopt solver - solved with simplex algorithm.

    Includes lower bounds for variables only, as well as linear constraints.

    Problem:
    Maximize:     z = 6x₁ + 14x₂ + 13x₃

    Subject to:   0.5x₁ + 2x₂ + x₃ ≤ 24
                  x₁ + 2x₂ + 4x₃ ≤ 60
                  x₁ ≥ 0, x₂ ≥ 0, x₃ ≥ 0
'''

from ortools.math_opt.python import mathopt

model = mathopt.Model(name='Linear Programming')

x1 = model.add_variable(name='x1', lb=0)
x2 = model.add_variable(name='x2', lb=0)
x3 = model.add_variable(name='x3', lb=0)

model.add_linear_constraint(0.5*x1 + 2*x2 + x3 <= 24)
model.add_linear_constraint(x1 + 2*x2 + 4*x3 <= 60)

model.maximize(6*x1 + 14*x2 + 13*x3)

result = mathopt.solve(model, mathopt.SolverType.GLOP)

# print solution
print("MathOpt solve succeeded")
print("Optimal Objective value:", result.objective_value())
print("x1:", result.variable_values()[x1])
print("x2:", result.variable_values()[x2])
print("x3:", result.variable_values()[x3])


'''
Output: 

Number of variables = 3
Number of constraints = 2
Solving with Glop solver v9.12.4544

Solution:
Objective value = 294.0
x1 = 36.0 (36 x 600 = $21,600 profit)
x2 = 0.0 (0 x 1,400 = $0 profit)
x3 = 6.0 (6 x 1,300 = $7,800 profit)

Explanation: 
Therefore, the optimal solution is producing 36 flat beds, 0 economy, and 6 luxury trailers for a total profit of $29,400 within the given constraints.

'''
