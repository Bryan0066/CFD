from prettytable import PrettyTable
import numpy as math
from sympy import *

XL, XU, p, mu, D = .00001, 1, 1.23, 1.79*10**-5, .5

List1 = ["", 1, 0.5411, 0.4588, 0.2512, 0.2075, 0.1239, 0.0836, 0.2075, 0.4588]

j = 7

V = (4*List1[j])/(math.pi*D**2)

Re = (p*V*D)/mu


def func(f):
    return float(4*math.log10(Re*math.sqrt(f))-.4-(1/math.sqrt(f)))


def dxfunc(f):
    return float((1/(2*f**(3/2)))+(.868589/f))


t = PrettyTable(["Iteration", "X", "EA"])  # headers

EA, x, xp, i = 100, float(.0035), float(.003), 0

t.add_row((i, "%.6f" % x, "%.6f" % EA))


while EA > .001:
    i = i + 1
    z = float(func(x))
    g = float(dxfunc(x))
    x1 = float(x-(z/g))
    EA = abs((x1 - x) / x1) * 100
    x = x1
    t.add_row([i, "%.6f" % x, "%.6f" % EA])
print(t)
