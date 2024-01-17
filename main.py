# x = 10
# y = 20
# print(x + y)
#
#
#
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
#
#
#
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
#
#
#
# def print_arguments(*args, **kwargs):
#     print("Positional arguments:")
#     for arg in args:
#         print(arg)
#     print("Keyword arguments:")
#     for key, value in kwargs.items():
#         print(key, ":", value)
# print_arguments("apple", "banana", "cherry", color="red", taste="sweet")
#
#
#
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# rect = Rectangle(5, 3)
# area = rect.area()
# perimeter = rect.perimeter()
# print(area) # 15
# print(perimeter) # 16
#
#
#
#
# # Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("The animal makes a sound.")
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#     def speak(self):
#         print("The dog barks: Woof!")
#     def fetch(self):
#         print("The dog fetches a ball.")
#
# from functions import get_date
# print(get_date())
#
#
#
#
#
#
#
# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Call the decorated function
#         result = func(*args, **kwargs)
#         # Convert the result to uppercase
#         return result.upper()
#     return wrapper
#
# @uppercase_decorator
# def say_hello(name):
#     print("Hello, {name}!")
# @uppercase_decorator
# def concatenate_strings(a, b):
#     return a + b
# # Example usage
# print(say_hello("Alice"))  # Output: HELLO, ALICE!
# print(concatenate_strings("Hello", "World"))  # Output: HELLOWORLD
#
#
#
#
#
#
#
#
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print("Executed {func.__name__} in {execution_time:.4f} seconds")
#         return result
#     return wrapper
#
# @timer
# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n - 1)
#
# factorial_result = calculate_factorial(10)
# print("Factorial of 10: {factorial_result}")


# num1 = 690430976
# num2 = 0
# str = "*"
#
# if num2 == 0:
#     print("Can't divide by 0")
# else:
#     if str == "+":
#         print(num1 + num2)
#     elif str == "-":
#         print(num1 - num2)
#     elif str == "*":
#         print(num1 * num2)
#     elif str == "/":
#         print(num1 / num2)
#     else:
#         print("Invalid operator")

# import os

# def main():

#     print(os.cpu_count())

# main()


# def memoize(func):
#     cache = {}

#     def wrapper(*args):
#         if args not in cache:
#             result = func(*args)
#             cache[args] = result
#             return result
#         else:
#             print(f"Returning cached result for {func.__name__}{args}")
#             return cache[args]

#     return wrapper

# @memoize
# def add(x, y):
#     print(f"Adding {x} and {y}")
#     return x + y

# @memoize
# def multiply(x, y):
#     print(f"Multiplying {x} and {y}")
#     return x * y

# # Testing the memoization
# print(add(2, 3))  # New calculation
# print(add(2, 3))  # Cached result
# print(multiply(4, 5))  # New calculation
# print(multiply(4, 5))  # Cached result


# result1 = input()
# result2 = input()
# result3 = input()
# if result1.isnumeric() and result2.isnumeric() and result3.isnumeric():
#     result1 = int(result1) / 100 * 30
#     result2 = int(result2) / 100 * 30
#     result3 = int(result3) / 100 * 40
#     finalResult = result1 + result2 + result3
#
#     if finalResult < 40:
#         print("Bad")
#     elif finalResult < 70:
#         print("Good")
#     elif finalResult < 90:
#         print("Very Good")
#     else:
#         print("Excellent")
# else:
#     print("The results should be numeric")
