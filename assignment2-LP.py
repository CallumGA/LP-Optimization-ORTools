'''
300501101 - Callum Anderson
Assignment 2, Q2, Pt. 2 (bonus)

Model:
min
    150y1 + 140y2 + 130y3 + 9x1A + 5x1B + 3x2A + 7x2B + 4x3A + 8x3B
s.t.
    x1A + x1B ≤ 60y1
    x2A + x2B ≤ 57y2
    x3A + x3B ≤ 50y3
    x1B + x2B  + x3B = 80 (customer B)
    x1A + x2A + x3A = 70 (customer A)
    xfc ≥ 0, yf element of {0,1}
'''

import pulp as pl

model = pl.LpProblem("Motor_Factory", pl.LpMinimize)

X = {(f, c): pl.LpVariable(f"X{f}{c}", lowBound=0)
     for f in [1, 2, 3] for c in ["A", "B"]}
y = {f: pl.LpVariable(f"y{f}", cat="Binary") for f in [1, 2, 3]}

model += (
    150*y[1] + 140*y[2] + 130*y[3]
    + 9*X[1,"A"] + 5*X[1,"B"]
    + 3*X[2,"A"] + 7*X[2,"B"]
    + 4*X[3,"A"] + 8*X[3,"B"]
)

model += X[1,"A"] + X[1,"B"] <= 60 * y[1]
model += X[2,"A"] + X[2,"B"] <= 57 * y[2]
model += X[3,"A"] + X[3,"B"] <= 50 * y[3]
model += X[1,"A"] + X[2,"A"] + X[3,"A"] == 70
model += X[1,"B"] + X[2,"B"] + X[3,"B"] == 80

status = model.solve(pl.PULP_CBC_CMD(msg=False))
print("Status:", pl.LpStatus[status])
print("Objective =", pl.value(model.objective))
for v in model.variables():
    print(v.name, "=", v.value())