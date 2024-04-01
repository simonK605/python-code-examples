import numpy as np


# Sample multidimensional list
multidimensional_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convert the list to a NumPy array
array_2d = np.array(multidimensional_list)

# Calculate the sum of the squares of columns
sum_of_squares = np.sum(array_2d**2, axis=0)

# Find the square root of the sum of the squares
result = np.sqrt(sum_of_squares)
print(result)