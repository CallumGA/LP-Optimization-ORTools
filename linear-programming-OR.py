'''
    Linear programming problem solved via OR tools solver - utilizing simplex method
'''

from ortools.linear_solver import pywraplp

# declare solver object
solver = pywraplp.Solver.CreateSolver('GLOP')

# declare variables (x1, x2, x3)
x1 = solver.NumVar(0, solver.infinity(), "x1")
x2 = solver.NumVar(0, solver.infinity(), "x2")
x3 = solver.NumVar(0, solver.infinity(), "x3")

print("Number of variables =", solver.NumVariables())

# define constraints

# must be less than or equal to 24 metal working days
solver.Add(0.5 * x1 + 2 * x2 + x3 <= 24)
# must be less than or equal to 60 wood working days
solver.Add(x1 + 2 * x2 + 4 * x3 <= 60)

print("Number of constraints =", solver.NumConstraints())

# define the objective function
z = solver.Maximize(6 * x1 + 14 * x2 + 13 * x3)

# solve
print(f"Solving with {solver.SolverVersion()}")
status = solver.Solve()

# print solution if feasible or infeasible
if status == pywraplp.Solver.OPTIMAL:
    print("\nSolution:")
    print(f"Objective value (best profit) = {solver.Objective().Value():0.1f}")
    print(f"x1 = {x1.solution_value():0.1f}")
    print(f"x2 = {x2.solution_value():0.1f}")
    print(f"x3 = {x3.solution_value():0.1f}")

else:
    print("The problem does not have an optimal solution.")
    
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

Explanation: Therefore, the optimal solution is producing 36 flat beds, 0 economy, and 6 luxury trailers for a total profit of $29,400 within the given constraints.
'''