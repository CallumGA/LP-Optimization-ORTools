'''
Notes:
    Visualize the LP model from pulp-LP.py using matplotlib.
    Plot only x1 and x2, since x3 is 0 in the final solution
'''

import itertools
import math
import numpy as np
import matplotlib.pyplot as plt
from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# ---------------------------
# 1. Build and solve the LP
# ---------------------------
model = LpProblem(name="LP-assignment-1", sense=LpMaximize)

x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)
x3 = LpVariable(name="x3", lowBound=0)  # will be zero for plotting

model += (-10 * x1 - 2 * x2 - x3 >= -100, "c1")
model += (7 * x1 + 3 * x2 + 2 * x3 <= 72,  "c2")
model += (2 * x1 + 4 * x2 + x3 <= 80,      "c3")

model += 22 * x1 + 6 * x2 + 2 * x3        # objective
model.solve()

opt_x1, opt_x2 = value(x1), value(x2)
print(f"Status: {LpStatus[model.status]}")
print(f"Optimal (x1,x2) = ({opt_x1:.2f}, {opt_x2:.2f})")
print(f"Objective value = {value(model.objective):.2f}")

# --------------------------------------
# 2. Define helper functions and lines
# --------------------------------------
def intersection(A, B, C, D):
    """Solve:
         A1*x + A2*y = A3
         B1*x + B2*y = B3
       where A=(A1,A2,A3) etc.  Returns (x,y) or None if lines are parallel."""
    a1, a2, a3 = A
    b1, b2, b3 = B
    det = a1 * b2 - a2 * b1
    if abs(det) < 1e-9:
        return None
    x = (a3 * b2 - a2 * b3) / det
    y = (a1 * b3 - a3 * b1) / det
    return (x, y)

# line coefficients in the form a1*x + a2*y = a3
L1 = (10, 2, 100)   # 10 x1 + 2 x2 = 100   (rewritten from -10x1-2x2 >= -100)
L2 = (7,  3, 72)    # 7  x1 + 3 x2 = 72
L3 = (2,  4, 80)    # 2  x1 + 4 x2 = 80

lines = [L1, L2, L3]

# ---------------------------------------------
# 3. Compute every candidate corner (vertices)
# ---------------------------------------------
candidates = [(0, 0)]  # origin is always feasible
# intersections of constraint lines
for (A, B) in itertools.combinations(lines, 2):
    pt = intersection(A, B, None, None)
    if pt:
        candidates.append(pt)
# intercepts with axes
for (a1, a2, a3) in lines:
    if a2 != 0:  # x-intercept (y=0)
        candidates.append((a3 / a1, 0))
    if a1 != 0:  # y-intercept (x=0)
        candidates.append((0, a3 / a2))

# keep only points satisfying *all* constraints and x>=0,y>=0
def feasible(x, y):
    return (
        (10 * x + 2 * y <= 100) and
        (7  * x + 3 * y <= 72)  and
        (2  * x + 4 * y <= 80)  and
        (x >= 0) and (y >= 0)
    )

vertices = [pt for pt in candidates if feasible(*pt)]

# order vertices counter-clockwise so that fill() draws a proper polygon
cx, cy = np.mean(vertices, axis=0)
vertices = sorted(vertices, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

# --------------------------------
# 4. Plot
# --------------------------------
fig, ax = plt.subplots()

# Draw constraint boundary lines
x_vals = np.linspace(0, max(v[0] for v in vertices) * 1.2, 400)
ax.plot(x_vals, (100 - 10 * x_vals) / 2, label="10 x₁ + 2 x₂ = 100")
ax.plot(x_vals, (72  - 7  * x_vals) / 3, label="7 x₁ + 3 x₂ = 72")
ax.plot(x_vals, (80  - 2  * x_vals) / 4, label="2 x₁ + 4 x₂ = 80")

# Shade the feasible region
poly = np.array(vertices + [vertices[0]])  # close polygon
ax.fill(poly[:, 0], poly[:, 1], alpha=0.3)

# Mark the optimal point
ax.scatter(opt_x1, opt_x2, marker='*', s=150, zorder=5, label="Optimal")

# Labels, limits, legend
ax.set_xlabel("x₁")
ax.set_ylabel("x₂")
ax.set_title("Feasible Region for LP-assignment-1 (x₃ = 0)")
ax.set_xlim(0)
ax.set_ylim(0)
ax.legend()
ax.grid(True)

plt.show()