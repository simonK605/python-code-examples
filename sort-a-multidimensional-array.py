# Example multidimensional array
multidimensional_array = [[1, 5, 3], [2, 3, 1], [4, 7, 2], [3, 2, 4]]

# Sort based on the second element of each subarray
sorted_array = sorted(multidimensional_array, key=lambda x: x[1])

# Display the sorted array
print(sorted_array)