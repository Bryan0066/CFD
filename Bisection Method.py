from prettytable import PrettyTable

XL, XU, x = .5, 2.5, 0
Xr = (XL + XU)/2
PE = abs((XU-XL)/(XU+XL)) * 100


def func(y):
    return 1-(400/(9.81*(3*y+(y**2)/2)**3))*(3+y)


t = PrettyTable(["Iteration", "Xl", "XU", "F(XL)", "F(XU)", "F(XR)*F(XU)", "XR", "F(XR)", "PE"])

t.add_row([x, "%.4f" % XL, "%.4f" % XU, "%.4f" % func(XL), "%.4f" % func(XU), "%.4f" % float(func(XL) * func(Xr)),
           "%.4f" % Xr, "%.4f" % func(Xr), "%.4f" % PE])

while PE > 1 and x < 10:

    if func(XL)*func(Xr) < 0:

        XU = Xr

    else:

        XL = Xr

    Xr = (XL + XU) / 2

    PE = abs((XU - XL) / (XU + XL)) * 100

    x = x+1

    t.add_row([x, "%.4f" % XL, "%.4f" % XU, "%.4f" % func(XL), "%.4f" % func(XU), "%.4f" % float(func(XL) * func(Xr)),
               "%.4f" % Xr, "%.4f" % func(Xr), "%.4f" % PE])

print(t)

end = input()
