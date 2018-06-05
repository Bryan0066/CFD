from prettytable import PrettyTable
import numpy as math

XL, XU, EA, x, p, mu, D = .00001, 1, 100, 0, 1.23, 1.79*10**-5, .5


List1 = ["null", "null", 0.5411, 0.4588, 0.2512, 0.2075, 0.1239, 0.0836, 0.2075, 0.4588]
#  list 1 contains flow rates for all the pipes (starting at 2)

print('Which pipe?')

j = int((input()))

V = (4*List1[j])/(math.pi*D**2)

Re = (p*V*D)/mu


def func(f):
    return 4*math.log10(Re*math.sqrt(f))-.4-(1/math.sqrt(f))


t = PrettyTable(["Iteration", "Xl", "XU", "F(XL)", "F(XU)", "F(XR)*F(XU)", "XR", "F(XR)", "EA"])

# Creates headers

Xr = XU - (func(XU)*(XL-XU))/(func(XL)-func(XU))

t.add_row([x, "%.5f" % XL, "%.5f" % XU, "%.5f" % func(XL), "%.5f" % func(XU), "%.5f" % float(func(XL) * func(Xr))
              , "%.5f" % Xr, "%.5f" % func(Xr), "%.5f" % EA])
# adds first (iteration 0) iteration to table
while EA > .001:
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

