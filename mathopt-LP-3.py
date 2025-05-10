'''
    Linear programming problem solved via OR tools mathopt solver - solved with simplex algorithm.

    Includes lower bounds for variables only, as well as linear constraints.

    Problem:
    Maximize:     z = 6x₁ + 14x₂ + 13x₃

    Subject to:   0.5x₁ + 2x₂ + x₃ ≤ 24
                  x₁ + 2x₂ + 4x₃ ≤ 60
                  x₁ ≥ 0, x₂ ≥ 0, x₃ ≥ 0
'''

from ortools.math_opt.python import mathopt

