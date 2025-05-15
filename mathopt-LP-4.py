'''
max ▪
    5𝑥1 + 2𝑥2 + 30𝑥3

    ▪ 𝑥1 + 9𝑥2 + 12𝑥3 ≤ 180
    ▪ 2𝑥1 + 9𝑥2 + 6𝑥3 ≤ 210
    ▪ 𝑥1, 𝑥2, 𝑥3 ≥ 0
'''

from ortools.math_opt.python import mathopt

model = mathopt.Model(name='Linear Programming')

x1 = model.add_variable(name='x1', lb=0)
x2 = model.add_variable(name='x2', lb=0)
x3 = model.add_variable(name='x3', lb=0)

model.add_linear_constraint(x1 + 9*x2 + 12*x3 <= 180)
model.add_linear_constraint(2*x1 + 9*x2 + 6*x3 <= 210)

model.maximize(5*x1 + 2*x2 + 30*x3)

result = mathopt.solve(model, mathopt.SolverType.GLOP)

print("MathOpt solve succeeded")
print("Optimal Objective value:", result.objective_value())
print("x1:", result.variable_values()[x1])
print("x2:", result.variable_values()[x2])
print("x3:", result.variable_values()[x3])