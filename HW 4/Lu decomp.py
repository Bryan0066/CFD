
import pprint

import scipy.linalg  # SciPy Linear Algebra Library

A = scipy.array([[75, -20, 0, 19.62], [-20, 35, -15, 29.43], [0, -15, 15, 14.715]])
P, L, U = scipy.linalg.lu(A)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

x3 = U[2, 3] / U[2, 2]
print("X3:", x3)

x2 = (U[1, 3] - (U[1, 2] * x3)) / U[1, 1]
print("X2:", x2)

x1 = (U[0, 3] + (U[0, 2] * x3) - U[0, 1] * x2) / U[0, 0]
print("X1:", x1)
