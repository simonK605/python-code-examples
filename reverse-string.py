def reverse_string(input_string):
    """
    Reverse a string using slicing.

    Parameters:
    - input_string (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    reversed_string = input_string[::-1]
    return reversed_string


# Example usage
original_string = "Hello, World!"
reversed_result = reverse_string(original_string)
print(reversed_result)
