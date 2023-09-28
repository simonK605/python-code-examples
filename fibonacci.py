import functools

def cache(func):
    memo = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test the cached Fibonacci function
print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(20))