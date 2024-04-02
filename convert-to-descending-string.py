def convert_to_descending_string(numbers):
    """
    Convert a list of integers to a string in descending order.

    Parameters:
    - numbers (list of int): The list of integers to be converted.

    Returns:
    - str: A string containing the sorted integers in descending order.
    """
    if not isinstance(numbers, (list, tuple)):
        raise ValueError("Input 'numbers' must be a list or tuple")

    # Check if numbers is empty
    if not numbers:
        raise ValueError("Input 'numbers' is empty")

    # Check if all elements in numbers are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in 'numbers' must be integers")

    # Sort the list of integers in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Convert the sorted list to a string
    result_string = ', '.join(map(str, sorted_numbers))

    return result_string


# Example usage:
my_numbers = [5, 12, 8, 3, 20]
result = convert_to_descending_string(my_numbers)

print(result)
