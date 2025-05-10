'''
    Linear programming problem built, solved and explored with MathOpt

    Problem:

    Maximize:     x + 2y

    Subject to:   x + y ≤ 1.5
                 -1 ≤ x ≤ 1.5
                  0 ≤ y ≤ 1
'''

from ortools.math_opt.python import mathopt

# define and build the model - this can can be solved using various solvers like GLOP
model = mathopt.Model(name="LP-example")
# define and add x and y variables with upper and lower bounds
x = model.add_variable(lb=-1.0, ub=1.5)
y = model.add_variable(lb=0.0, ub=1.0)
# add the constraint for the model
model.add_linear_constraint(x + y <= 1.5)
# maximize the model
model.maximize(x + 2 * y)

# solve
result = mathopt.solve(model, mathopt.SolverType.GLOP)
if result.termination.reason != mathopt.TerminationReason.OPTIMAL:
    raise RuntimeError(f"model failed to solve: {result.termination}")

# print solution
print("MathOpt solve succeeded")
print("Objective value:", result.objective_value())
print("x:", result.variable_values()[x])
print("y:", result.variable_values()[y])

'''
Output: 
MathOpt solve succeeded
Objective value: 2.5
x: 0.5
y: 1.0

Explanation: 
With x as 0.5 and y as 1.0, these variables are optimized to produce the best outcome for the function we are trying to maximize: x + 2 * y.
When x=0.5 and y=1.0 are plugged into x + 2 * y, the function is maximized for an objective value result of 2.5, falling within constraints defined. 

'''