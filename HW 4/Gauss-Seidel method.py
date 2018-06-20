
import numpy as np
from prettytable import PrettyTable
import pprint as p

Q2, Q3, Q4, Q5, Q6, Q7, lam = 0, 0, 0, 0, 0, 0, .95
x1, x2, x3 = 0,0,0
x = 0

a = np.array([[-2,1,2,0,0,0],[1,1,0,0,0,0],[0,1,-1,1,0,0],[0,0,0,1,-1,-1],[0,0,-2,1,2,0],[0,0,0,0,2,3]])

b =np.array([[0],[1],[0],[0],[0],[0]])
A = np.array([0,0,0,0,0,0])
p.pprint(A)
p.pprint(b)

while x <= 2:

    Q2p = (-Q3-2*Q4)/-2
    Q2 = lam*Q2p+(1-lam)*Q2


    Q3p = (-1+Q2)/-1
    Q3 = lam*Q3p+(1-lam)*Q3


    Q4p = (-Q5-2*Q6)/-2
    Q4 = lam *Q4p+(1-lam)*Q4


    Q5p = (-Q3+Q4)/-1
    Q5 = lam*Q5p+(1-lam)*Q5


    Q6p = (-3*Q7)/-2
    Q6 = lam*Q6p+(1-lam)*Q6


    Q7p = (-Q5+Q6)/-1
    Q7 = lam*Q7p+(1-lam)*Q7



    newrow = [Q2, Q3, Q4, Q5, Q6, Q7]
    A = np.vstack([A,newrow])

    x += 1
print(A)
"""
    x += 1
    x1s = (3+x2+x3)/6
    x1p = lam * (x1s) + (1 - lam) * x1


    x2s = (40 - 6*x1p - x3) / 9
    x2p = lam * (x2s) + (1 - lam) * x2

    x3s = (50 + 3*x1p - x2p) / 12
    x3p = lam * (x3s) + (1 - lam) * x3

    x1 = x1p
    x2 = x2p
    x3 = x3p
    x +=1
    print(x1, x2, x3)

0.505882352941176
0.494117647058824
0.258823529411765
0.235294117647059
0.141176470588235
0.0941176470588235"""
'''
c+2d-2b=0
e+2f-2d=0
3g-2f=0
b+c=1
c=d+e
e=f+g'''

