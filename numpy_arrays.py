import numpy as np

# Create NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

# Print the arrays
print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

# Basic operations
print("\nBasic operations:")
print("Sum of array 1:", np.sum(arr1))
print("Mean of array 1:", np.mean(arr1))
print("Minimum value in array 1:", np.min(arr1))
print("Maximum value in array 1:", np.max(arr1))

# Indexing
print("\nIndexing:")
print("Element at index 2 of array 1:", arr1[2])
print("Element at row 1, column 2 of array 2:", arr2[1, 2])

# Slicing
print("\nSlicing:")
print("First three elements of array 1:", arr1[:3])
print("Last two elements of array 1:", arr1[-2:])
print("Second row of array 2:", arr2[1, :])

# Reshaping
print("\nReshaping:")
arr3 = np.arange(12)  # Create a 1D array with values from 0 to 11
reshaped_arr3 = arr3.reshape(3, 4)  # Reshape the array to a 3x4 matrix
print("Original array:")
print(arr3)
print("Reshaped array:")
print(reshaped_arr3)
