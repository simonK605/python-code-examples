import os
import platform

path = os.path.expanduser("~/Desktop")


def handle_32_bit():
    # Handle 32-bit OS functionality
    pass


def handle_64_bit():
    # Handle 64-bit OS functionality
    pass


if platform.architecture()[0] == '32bit':
    handle_32_bit()
else:
    handle_64_bit()
