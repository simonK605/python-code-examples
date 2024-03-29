def memoize(func):
    """
    Decorator function to memoize the results of function calls.

    Args:
        func (function): The function to be memoized.

    Returns:
        function: The wrapper function that memoizes the results.
    """
    cache = {}

    def wrapper(*args):
        """
        Wrapper function that memoizes the results of the decorated function.

        Args:
            *args: Positional arguments passed to the decorated function.

        Returns:
            Any: The result of the decorated function.
        """
        if args not in cache:
            # If result is not cached, call the decorated function and store the result in the cache
            result = func(*args)
            cache[args] = result
            return result
        else:
            # If result is cached, return the cached result
            print(f"Returning cached result for {func.__name__}{args}")
            return cache[args]

    return wrapper

@memoize
def add(x, y):
    """
    Function to add two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    print(f"Adding {x} and {y}")
    return x + y

@memoize
def multiply(x, y):
    """
    Function to multiply two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    print(f"Multiplying {x} and {y}")
    return x * y

# Testing the memoization
print(add(2, 3))  # New calculation
print(add(2, 3))  # Cached result
print(multiply(4, 5))  # New calculation
print(multiply(4, 5))  # Cached result