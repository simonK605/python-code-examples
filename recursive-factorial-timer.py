import time


def timer(func):
    """
    Decorator function to measure the execution time of another function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapper function that measures the execution time.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function that measures the execution time of the decorated function.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            Any: The result of the decorated function.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Executed {func.__name__} in {execution_time:.4f} seconds")
        return result

    return wrapper


@timer
def calculate_factorial(n):
    """
    Function to calculate the factorial of a number recursively.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


factorial_result = calculate_factorial(10)
print(f"Factorial of 10: {factorial_result}")
