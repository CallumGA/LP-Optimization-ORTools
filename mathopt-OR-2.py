'''
    Linear programming problem solved via OR tools mathopt solver - solved with simplex algorithm.

    Problem:

    Maximize:     3x + 4y

    Subject to:   x + 2y ≤ 14
                  3x - y ≥ 0
                  x - y ≤ 2
'''

from ortools.math_opt.python import mathopt

