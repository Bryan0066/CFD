from prettytable import PrettyTable
import sympy as sym

Wo, L, E, y, I = 15, 3, 70, .009, 52.9*10**-6


def func(v):
    return (Wo*L)/(3*(3.14**4)*E*I)*(48*(L**3)*sym.cos((3.14/2*L)*v)-(48*(L**3))+(3*3.14**3*L*v**2)-(3.14**3*v**3))-y


t = PrettyTable(["Iteration", "X", "EA"])  # headers

EA, x, xp, i = 100, 1.8, 1.9, 0

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
