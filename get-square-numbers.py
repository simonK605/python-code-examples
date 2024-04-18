import math
from typing import Any


def get_square_numbers(nums: list) -> list[Any]:
    """
    Finds and returns the square numbers from a list of integers.

    Parameters:
        nums (list): A list of integers.

    Returns:
        list: A list containing the square numbers from the input list.
    """
    square_numbers = []

    # Iterate through each number in the input list
    for num in nums:
        # Check if the number is a perfect square
        if math.isqrt(num) ** 2 == num:
            # If it is a perfect square, add it to the list of square numbers
            square_numbers.append(num)

    return square_numbers


# Test the get_square_numbers function with a sample list
print(get_square_numbers([4, 10, 9, 8, 25]))
