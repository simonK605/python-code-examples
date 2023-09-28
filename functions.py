import datetime
from functools import cache


def get_date():
    return datetime.datetime.now()


@cache
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# First call - Sum will be calculated
print(calculate_sum([1, 2, 3, 4, 5])) # Output: 15
# Second call - Cached result will be returned
print(calculate_sum([1, 2, 3, 4, 5])) # Output: 15
