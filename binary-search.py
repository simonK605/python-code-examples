def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.

    Parameters:
    - arr (list): The sorted list to search.
    - target (int): The target element to find in the array.

    Returns:
    - int: The index of the target element if found, otherwise -1.

    Time Complexity:
    - O(log n), where n is the length of the array.

    Space Complexity:
    - O(1), as the function uses a constant amount of extra space.
    """
    # Initialize the low and high pointers for the search range
    low, high = 0, len(arr) - 1

    # Continue the search until the search range is valid
    while low <= high:
        # Calculate the middle index
        mid = low + (high - low) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If the target is greater, narrow the search to the right half
        elif arr[mid] < target:
            low = mid + 1
        # If the target is smaller, narrow the search to the left half
        else:
            high = mid - 1

    # If the target is not found in the array, return -1
    return -1


# Example usage
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
