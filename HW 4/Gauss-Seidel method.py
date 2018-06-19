
from numpy import matrix
import numpy as np
from numpy.linalg import inv

import numpy as np
from scipy.linalg import solve
'''
A = np.array([[-2,1,2,0,0,0],[0,0,2,1,2,0],[0,0,0,0,-2,3],[1,1,0,0,0,0],[0,-1,1,1,0,0],[0,0,0,-1,1,1]])

b =np.array([[0,0,0,1,0,0]])





x1 = (1/(A[0,0]))(b[0]-A[2,1])


'''


'''
A = np.array([[16,3],[7, -11]])
b = np.array([[11],[13]])

L = np.array([[16,0],[7,-11]])
U = np.array([[0,3],[0,0]])
Lin = inv(L)




print(A)
print(b)
print(Lin)'''
'''
b =np.array([[0,0,0,1,0,0]])

Q1 = 1
Q2 = 0
Q3 = 0
Q4 = 0
Q5 = 0
Q6 = 0
Q7 = 0



Q1 = Q2 + Q3
Q3 = Q4 + Q5
Q4 = (Q5+2*Q6)/2
Q5 = 2*(Q6-Q4)
Q6 = (2*Q4-Q5)/2
Q7 = 
'''



"""""
A = np.array([[-2,1,2,0,0,0],[0,0,2,1,2,0],[0,0,0,0,-2,3],[1,1,0,0,0,0],[0,-1,1,1,0,0],[0,0,0,-1,1,1]])

b =np.array([[0],[0],[0],[1],[0],[0]])

x = solve(A,b)

print(np.dot(A,x)-b)


x = np.linalg.lstsq(A,b)

print(x)"""




# -*- coding: utf-8 -*-

"""
Gauss Seidelova methoda.
"""

