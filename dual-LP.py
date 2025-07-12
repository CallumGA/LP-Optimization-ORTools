"""
300501101 - Callum Anderson
Assignment 2, Q1, Pt. 2

max:    21y1 + 19y2
s.t:    4y1 + 2y2 ≤ 5
        2y1 + 4y2 ≤ 6
        y1, y2 ≥ 0
"""

from pulp import LpProblem, LpVariable, LpStatus, PULP_CBC_CMD, LpMaximize

model = LpProblem(name="Dual-LP-assignment-2", sense=LpMaximize)

y1 = LpVariable(name="y1", lowBound=0) # lowBound = 0 covers "y1, y2 ≥ 0"
y2 = LpVariable(name="y2", lowBound=0)

model += (4 * y1 + 2 * y2 <= 5, "y1")
model += (2 * y1 + 4 * y2 <= 6, "y2")

model += 21 * y1 + 19 * y2

model.solve(PULP_CBC_CMD(msg=False))

print(f"Status: {LpStatus[model.status]}")
print(f"y1 = {y1.value()}")
print(f"y2 = {y2.value()}")
print(f"Objective value = {model.objective.value()}")
