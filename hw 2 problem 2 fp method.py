from prettytable import PrettyTable
import numpy as math

XL, XU, EA, Q, g, x = .5, 2.5, 100, 20, 9.81, 0
# define variables

def func(y):
    return float(1-((Q**2)/(g*(3*y+((y**2)/2))**3))*(3+y))


t = PrettyTable(["Iteration", "Xl", "XU", "F(XL)", "F(XU)", "F(XR)*F(XU)", "XR", "F(XR)", "EA"])
# Creates headers


Xr = XU - (func(XU)*(XL-XU))/(func(XL)-func(XU))

t.add_row([x, "%.5f" % XL, "%.5f" % XU, "%.5f" % func(XL), "%.5f" % func(XU), "%.5f" % float(func(XL) * func(Xr))
              , "%.5f" % Xr, "%.5f" % func(Xr), "%.5f" % EA])
# adds first (iteration 0) iteration to table
while EA > 1 and x < 10:
    if func(XL)*func(Xr) < 0:

        XU = Xr

    else:

        XL = Xr

    Xrl = Xr
    Xr = XU - ((func(XU)*(XL - XU)) / (func(XL) - func(XU)))
    EA = abs(((Xr-Xrl)/Xr)*100)
    x = x+1

    t.add_row([x, "%.5f" % XL, "%.5f" % XU, "%.5f" % func(XL), "%.5f" % func(XU),
               "%.5f" % float(func(XL) * func(Xr)), Xr, "%.5f" % func(Xr), "%.5f" % EA])

print(t)
