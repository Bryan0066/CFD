from prettytable import PrettyTable
import sympy as sym
from sympy import *
import math as math

XL, XU, p, mu, D = .00001, 1, 1.23, 1.79*10**-5, .5

List1 = ["", 1, 0.50411, 0.4588, 0.2512, 0.2075, 0.1239, 0.0836, 0.2075, 0.4588]

j = 7

V = (4*List1[j])/(3.14*D**2)

Re = (p*V*D)/mu


def func(y):
    return 1-(400/(9.81*(3*y+(y**2)/2)**3))*(3+y)


f = sym.symbols('f')

fprime = sym.diff(func(f),f)


print('f prime = ',(fprime))



t = PrettyTable(["Iteration", "X", "EA"])  # headers

EA, x, xp, i = 100, float(.5), float(2.5), 0

t.add_row((i, x, EA))


while EA > .001:
    i = i + 1
    z = func(x)
    g = fprime.evalf(subs={f: x})
    x1 = x - (z / g)
    EA = abs((x1 - x) / x1) * 100
    x = x1
    t.add_row([i, x, EA])
print(t)
