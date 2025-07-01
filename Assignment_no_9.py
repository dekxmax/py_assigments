import numpy as np
print("QUESTION NO 1: combine 1d and 2d array")
arr1 = np.array([1,2])
arr2= np.array([[5,6],[7,9]])
arr_1 = arr1.reshape(1,2)
res = np.concatenate((arr2,arr_1),axis=0)
print(res)
print("\n")
print("QUESTION NO 2 : flatten array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
flat = arr.flatten()
print(flat)
print("\n")
print("QUESTION NO 3:Reverse array ")
rev_arr = arr[::-1]
print(rev_arr)
print("\n")
print("QUESTION NO 4: Practice NumPy Operations")
arr = np.array([[10, 50, 30], [5, 20, 90]])
print("Array:\n", arr)
print("\n4.1) Maximum Value:", np.max(arr))
print("4.2) Minimum Value:", np.min(arr))
rows, cols = arr.shape
print("4.3) Number of Rows:", rows)
print("     Number of Columns:", cols)
print("\n4.4) Accessing each element:")
for i in range(rows):
    for j in range(cols):
        print(f"Element at ({i},{j}) = {arr[i][j]}")

print("\n4.5) Specific Element at row 1, col 2:", arr[1][2])  # Output: 90
total = 0
for row in arr:
    for value in row:
        total += value
print("4.6) Total Sum of Elements (using loop):", total)
print("\n4.7) Arithmetic Operations:")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("a:\n", a)
print("b:\n", b)

print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Division:\n", a / b)
