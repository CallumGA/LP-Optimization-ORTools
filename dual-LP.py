"""
300501101 - Callum Anderson
Assignment 2, Q1, Pt. 2

min:    5x1 + 6x2 
s.t:    4x1 + 2x2 ≥ 21
        2x1 + 4x2 ≥ 19
        x1, y1 ≥ 0
"""

from pulp import LpProblem, LpVariable, LpStatus, LpMinimize, PULP_CBC_CMD

model = LpProblem(name="Dual-LP-assignment-2", sense=LpMinimize)

x1 = LpVariable(name="x1", lowBound=0) # lowBound = 0 covers "x1, y1 ≥ 0"
x2 = LpVariable(name="x2", lowBound=0) # lowBound = 0 covers "x1, y1 ≥ 0"

model += (4*x1 + 2*x2 >= 21, "x1")
model += (2*x1 + 4*x2 >= 19, "x2")

model += 5*x1 + 6*x2

model.solve(PULP_CBC_CMD(msg=False))

print(f"Status: {LpStatus[model.status]}")
print(f"x1 = {x1.value()}")
print(f"x2 = {x2.value()}")
print(f"Objective value = {model.objective.value()}")
