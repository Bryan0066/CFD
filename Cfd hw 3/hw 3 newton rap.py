from prettytable import PrettyTable
import numpy as math
from sympy import *
XL, XU, g, Q = .00001, 1, 9.81, 20
from sympy import Symbol, Derivative


p, mu, D, EA, i= 1.23, 1.79*10**-5, .5, 100,0
List1 = ["", "", 0.5411, 0.4588, 0.2512, 0.2075, 0.1239, 0.0836, 0.2075, 0.4588]

print('Which pipe?')

j = int((input()))

V = (4*List1[j])/(math.pi*D**2)

Re = (p*V*D)/mu

def func(f):
    return (4*(Re*(y)**(1/2))-.4-(1/(y)**(1/2)))


y = Symbol('f')


function = (4*(Re*(y)**(1/2))-.4-(1/(y)**(1/2)))

deriv = Derivative(function, y)
deriv.doit().subs({y:4})


x, x1 = .003, .0035


t = PrettyTable(["Iteration", "X", "EA"])
t.add_row((i, "%.6f" % x, "%.6f" % EA))


while EA > .001:
    deriv = Derivative(function, y)
    deriv.doit().subs({y: x})
    i = i + 1
    z = func(x)
    g = deriv.doit().subs({y: x})
    x1 = x-(z/g)
    EA = abs((x1 - x) / x1) * 100
    x = x1
    t.add_row([i,  x,  EA])
print(t)