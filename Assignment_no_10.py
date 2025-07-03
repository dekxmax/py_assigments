import numpy as np
import matplotlib.pyplot as plt

print("QUESTION NO 1. Replace NaN with 0 and interchange rows and columns")
arr1 = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr1 = np.nan_to_num(arr1, nan=0)
arr1 = arr1[:, [2, 0, 1, 3]] 
arr1 = arr1[[1, 0], :]        
print(arr1)

print("\nQUESTION NO 2. Move axes of 3D array to new positions")
arr2 = np.arange(24).reshape(2, 3, 4)
arr2_moved = np.moveaxis(arr2, 0, -1)
print(arr2_moved)

print("\nQUESTION NO 3. Replace NaN values with average of columns")
arr3 = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
col_means = np.nanmean(arr3, axis=0)
inds = np.where(np.isnan(arr3))
arr3[inds] = np.take(col_means, inds[1])
print(arr3)

print("\nQUESTION NO 4. Replace negative value with zero in NumPy array using boolean indexing")
arr4 = np.array([[5, -1, 7], [-3, 8, -2]])
arr4[arr4 < 0] = 0
print(arr4)

print("\nQUESTION NO 5. Study the following program — already done below")

print("\nQUESTION NO 6. Create NumPy arrays")
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
print("arr1:", arr1)
print("arr2:", arr2)

print("\nQUESTION NO 7. Find average of NumPy arrays and calculate mean and median")
avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:", avg)

arr_2d_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d_2 = np.array([[6, 5, 4], [3, 2, 1]])
combined = np.concatenate((arr_2d_1, arr_2d_2), axis=0)

mean_val = np.mean(combined)
median_val = np.median(combined)

vals, counts = np.unique(combined, return_counts=True)
mode_val = vals[np.argmax(counts)]

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode (manual):", mode_val)

print("\nQUESTION NO 8. Solve equation using linalg() and inverse matrix method")

A = np.array([[1, -2, 3],
              [-1, 3, -2],
              [2, -5, 5]])
B = np.array([9, -6, 17])

solution, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)
print("Solution using least squares:", solution)

try:
    inv_method = np.dot(np.linalg.inv(A), B)
    print("Solution using inverse matrix:", inv_method)
except np.linalg.LinAlgError:
    print("Matrix is singular, inverse method not applicable.")


print("\nQUESTION NO 9. Compare at least 2 semester results using matplotlib")
semesters = ['Sem1', 'Sem2']
marks = [75, 85]

plt.bar(semesters, marks, color=['skyblue','orange'])
plt.title("Semester-wise Comparison")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.yticks(np.arange(0, 101, 10))
plt.show()
