def rotate_array(nums, k):
    """
    Rotate the elements of a list to the right by k steps.

    Args:
    nums (list): List of integers.
    k (int): Number of steps to rotate the list.

    Returns:
    list: The rotated list.
    """
    l = len(nums)
    k = k % l

    nums[:] = nums[-k:] + nums[:-k]

    return nums


# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array(nums, 3))
