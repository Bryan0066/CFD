from prettytable import PrettyTable
import math
import sympy as sym

Wo, L, E, y, I, pi, EA, x, i = 15*10**3, 3, 70*10**9, .009, 52.9*10**-6, math.pi, 100, 1.8, 0


def func(k):
    return ((Wo*L)/(3*pi**4*E*I))*(48*L**3*sym.cos((pi/(2*L))*k)-48*L**3+3*pi**3*L*k**2-pi**3*k**3)-y


v = sym.symbols('v')
fprime = sym.diff(func(v), v)
#  derives function

t = PrettyTable(["Iteration", "X", "Error"])  # headers for table

t.add_row((i, x, EA))   # adds row to table created by PrettyTable

while EA > .01:
    i = i + 1
    z = func(x)
    g = fprime.evalf(subs={v: x})
    x1 = x - (z / g)  # x1 is the next value for x
    EA = abs((x1 - x) / x1) * 100
    x = x1
    t.add_row([i, x, EA])
print(t)
