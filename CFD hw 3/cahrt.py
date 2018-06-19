from sympy import *
import math
import sympy as sym
import pandas as pd

Wo, L, E, y, I, pi, EA, x,= 15*10**3, 3, 70*10**9, .009, 52.9*10**-6, math.pi, 100, 1.8


def func(k):
    return ((Wo*L)/(3*pi**4*E*I))*(48*L**3*sym.cos((pi/(2*L))*k)-(48*L**3)+(3*pi**3*L*k**2)-(pi**3*k**3))-y


v = sym.symbols('v')
fprime = sym.diff(func(v), v)
#  derives function
EAa = [EA]
xa = [x]

while EA > .01:
    z = func(x)
    g = fprime.evalf(subs={v: x})
    x1 = x - (z / g)
    EA = abs((x1 - x) / x1) * 100
    xa.append(round(x1,5))
    EAa.append(round(EA,5))
    x = x1

df = pd.DataFrame()
xs = pd.Series(xa)
EAs = pd.Series(EAa)
df['x'] = xs.values
df['EA'] = EAs.values
print(df)

# https://stackoverflow.com/questions/32138205/convert-list-to-a-1-column-panda-dataframe
#  https://stackoverflow.com/questions/26666919/python-pandas-add-column-in-dataframe-from-list/38490727