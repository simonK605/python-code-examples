def uppercase_decorator(func):
    """
    Decorator function to convert the result of a function to uppercase.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapper function that converts the result to uppercase.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function that calls the decorated function and converts the result to uppercase.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            str: The result of the decorated function converted to uppercase.
        """
        # Call the decorated function
        result = func(*args, **kwargs)
        # Convert the result to uppercase
        return result.upper()

    return wrapper


@uppercase_decorator
def say_hello(name):
    """
    Function to greet a person with their name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: The greeting message.
    """
    print(f"Hello, {name}!")


@uppercase_decorator
def concatenate_strings(a, b):
    """
    Function to concatenate two strings.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return a + b


# Example usage
print(say_hello("Alice"))  # Output: HELLO, ALICE!
print(concatenate_strings("Hello", "World"))  # Output: HELLOWORLD
