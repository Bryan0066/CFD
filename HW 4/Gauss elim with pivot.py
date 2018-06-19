from numpy import matrix

a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
R1i = matrix([75, -20, 0, 19.62])
R2i = matrix([-20, 35, -15, 29.43])
R3i = matrix([0, -15, 15, 14.715])
R1 = matrix([])
R2 = matrix([])
R3 = matrix([])
R1ii = matrix([])
R2ii = matrix([])

''' t = 0
print('Gaussian elimination')
print("System of equations in the form....")
print()
print('a11+a12+a13+a14')
print('a21+a22+a23+a24')
print('a31+a32+a33+a34')
print()

while t == 0:
    print('Type a11')
    a11 =float(input())
    print('Type a12')
    a12 =float(input())
    print('Type a13')
    a13 =float(input())
    print('Type a14')
    a14 =float(input())

    R1 = matrix((a11,a12,a13,a14))
    z = 1

    while z != "y" and z != "n":
        print("is this correct for row 1? Type y for yes, n for no", R1)
        z = input()
        if z == "y":
            print("Row 1, complete")
            t = 1

        elif z == "n":
            print("Please correctly enter row 1")

b = 0
while b == 0:
    print('Type a21')
    a21 =float(input())
    print('Type a22')
    a22 =float(input())
    print('Type a23')
    a23 =float(input())
    print('Type a24')
    a24 =float(input())

    R2 = matrix((a21,a22,a23,a24))
    t1 = 1

    while t1 != "y" and t1 != "n":
        print("is this correct for row 2? Type y for yes, n for no", R2)
        t1 = input()
        if t1 == "y":
            print("Row 2, complete")
            b = 1

        elif t1 == "n":
            print("Please correctly enter row 2")

c = 0
while c == 0:
    print('Type a31')
    a31 =float(input())
    print('Type a32')
    a32 =float(input())
    print('Type a33')
    a33 =float(input())
    print('Type a34')
    a34 =float(input())
    R3 = matrix((a31,a32,a33,a34))
    t2 = 1

    while t2 != "y" and t2 != "n":
        print("is this correct for row 2? Type y for yes, n for no", R3)
        t2 = input()
        if t2 == "y":
            print("Row 2, complete")
            c = 1
        elif t2 == "n":
            print("Please correctly enter row 2")'''

#  first pivot

if R1i.item(0) > R2i.item(0) > R3i.item(0):
    R1 = R1i
    R2 = R2i
    R3 = R3i

elif R1i.item(0) > R3i.item(0) > R2i.item(0):
    R1 = R1i
    R2 = R3i
    R3 = R2i

elif R2i.item(0) > R1i.item(0) > R3i.item(0):
    R1 = R2i
    R2 = R1i
    R3 = R3i

elif R2i.item(0) > R3i.item(0) > R1i.item(0):
    R1 = R2i
    R2 = R3i
    R3 = R1i

elif R3i.item(0) > R1i.item(0) > R2i.item(0):
    R1 = R3i
    R2 = R1i
    R3 = R2i

elif R3i.item(0) > R2i.item(0) > R1i.item(0):
    R1 = R3i
    R2 = R2i
    R3 = R1i

# prints out matrix after first pivot

print(R1)
print(R2)
print(R3)
print()

#  Row 1 * multiplier - Row 2 step

R1m = float(R2.item(0) / R1.item(0))
R1p = R1 * R1m
R2f = R1p - R2

# second pivot

if R2f.item(0) > R3.item(0):
    R2ii = R2f
    R3ii = R3
else:
    R3ii = R2f
    R2ii = R3

# Row 1 * multiplier - Row 3 step

R1mm = float(R3.item(0) / R1.item(0))
R1pp = R1 * R1mm
R3 = R1pp - R3

# Row 2 * multiplier - Row 3 step

R2m = (R3.item(1) / R2f.item(1))
R2pp = R2f * R2m
R3f = R2pp - R3

# reference R3f, R2f, and R1

# Calculate X1,X2,X3

x3 = R3f.item(3) / R3f.item(2)
print("X3:", x3)
x2 = (R2f.item(3) - (R2f.item(2) * x3)) / R2f.item(1)
print("X2:", x2)
x1 = (R1.item(3) + (R1.item(2) * x3) - R1.item(1) * x2) / R1.item(0)
print("X1:", x1)