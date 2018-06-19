import pprint

import scipy.linalg   # SciPy Linear Algebra Library

k1, k2 ,k3, k4,m1,m2,m3,g = 30, 25 ,20 ,15 ,2 ,3 ,1.5 ,9.81



a = []
b = []
c = []

v =(k1+k2+k3)


a.extend((k1+k2+k3,-k3,0,m1*g))
b.extend((-k3,k3+k4,-k4,m2*g))
c.extend((0,-k4,k4,m3*g))

A = scipy.array([ a, b, c])

P, L, U = scipy.linalg.lu(A)


print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)


x3 = U[2,3]/U[2,2]
print("U3:", x3)

x2 = (U[1,3]-(U[1,2]*x3))/U[1,1]
print("U2:", x2)

x1 = (U[0,3]+(U[0,2]*x3)-U[0,1]*x2)/U[0,0]
print("U1:", x1)

# https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy
