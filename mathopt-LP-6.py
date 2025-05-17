'''
300501101 - Callum Anderson
Assignment 1, Q2, Pt. 2

Model:
max
    22x1 + 6x2 + 2x3
s.t.
    -10x1 - 2x2 - x3 ≥ -100
    7x1 + 3x2 + 2x3 ≤ 72
    2x1 + 4x2 +x3 ≤ 80
    x1,x2,x3 ≥ 0
'''

from ortools.math_opt.python import mathopt

model = mathopt.Model(name='Linear Programming')

x1 = model.add_variable(name='x1', lb=0)
x2 = model.add_variable(name='x2', lb=0)
x3 = model.add_variable(name='x3', lb=0)

model.add_linear_constraint(-10*x1 - 2*x2 - x3 >= -100)
model.add_linear_constraint(7*x1 + 3*x2 + 2*x3 <= 72)
model.add_linear_constraint(2*x1 + 4*x2 + x3 <= 80)

model.maximize(22*x1 + 6*x2 + 2*x3)

result = mathopt.solve(model, mathopt.SolverType.GLOP)

print("MathOpt solve succeeded")
print("Optimal Objective value:", result.objective_value())
print("x1:", result.variable_values()[x1])
print("x2:", result.variable_values()[x2])
print("x3:", result.variable_values()[x3])