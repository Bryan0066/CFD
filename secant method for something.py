from prettytable import PrettyTable
import numpy as math
XL, XU, g, Q = .00001, 1, 9.81, 20


def func(y):
    return float(1-((Q**2)/(g*(3*y+((y**2)/2))**3))*(3+y))


t = PrettyTable(["Iteration", "X", "EA"])  # headers

EA, x, xp, i = 100, float(.0035), float(.003), 0

t.add_row((i, "%.6f" % x, "%.6f" % EA))

while EA > .001:
    i = i + 1
    z = float(func(x)*(xp-x))
    g = float(func(xp)-func(x))
    x1 = float(x-(z/g))
    EA = abs((x1 - x) / x1) * 100
    xp = x
    x = x1
    t.add_row([i,  x,  EA])
print(t)
