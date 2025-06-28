import numpy as np

print("Q1: Various array creations")

print( "4x2 array")
a1 = np.random.rand(4, 2)
print(a1)

print("Empty and full arrays (4x2)")
a2 = np.empty((4, 2))
a3 = np.full((4, 2), 7)
print(a2)
print(a3)

print("Zeros array 3x5")
a4 = np.zeros((3, 5))
print(a4)

print("Ones array 4x3x2")
a5 = np.ones((4, 3, 2))
print(a5)

print("Q2: 3x3 matrix with values 2 to 10")
b = np.arange(2, 11).reshape(3, 3)
print(b)
print("Q3: Null vector size 10, set 6th element to 11")
c = np.zeros(10)
c[5] = 11
print(c)

print("Q4: Reverse an array")
d = np.array([1, 2, 3, 4, 5])
print(d)
d_rev = d[::-1]
print(d_rev)

print("Q5: Convert to float type")
e = np.array([10, 20, 30])
print(e)
e_float = e.astype(float)
print(e_float)
