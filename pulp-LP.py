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

from pulp import LpProblem, LpMaximize, LpVariable, LpStatus

model = LpProblem(name="LP-assignment-1", sense=LpMaximize)

x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)
x3 = LpVariable(name="x3", lowBound=0)

model += (-10*x1 - 2*x2 - x3 >= -100, "x1")
model += (7*x1 + 3*x2 + 2*x3 <= 72, "x2")
model += (2*x1 + 4*x2 + x3 <= 80, "x3")

model += 22*x1 + 6*x2 + 2*x3

model.solve()

print(f"Status: {LpStatus[model.status]}")
print(f"x1 = {x1.value()}")
print(f"x2 = {x2.value()}")
print(f"x3 = {x3.value()}")
print(f"Objective value = {model.objective.value()}")