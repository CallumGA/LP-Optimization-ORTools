'''
Model:

max
    z = 50,000x + 20,000y
s.t.
    25x + 12y ≤ 1400
    5y ≥ 2x
    x + 1/2y ≤ 20
    x, y ≥ 0 and x, y must be integers
'''

from ortools.math_opt.python import mathopt

model = mathopt.Model(name='Linear Programming')

x = model.add_variable(name='x', lb=0)
y = model.add_variable(name='y', lb=0)

model.add_linear_constraint(25*x + 12*y <= 1400)
model.add_linear_constraint(5*y >= 2*x)
model.add_linear_constraint(x + 0.5*y <= 20)

model.maximize(50000*x + 20000*y)

result = mathopt.solve(model, mathopt.SolverType.GLOP)

print("MathOpt solve succeeded")
print("Optimal Objective value:", result.objective_value())
print("x:", result.variable_values()[x])
print("y:", result.variable_values()[y])