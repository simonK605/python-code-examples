import ctypes


def get_screen_resolution() -> tuple:
    """
    Gets the screen resolution (width and height) of the user's monitor.

    Returns:
        tuple: A tuple containing the width and height of the screen resolution.
    """
    # Load the user32 library
    user32 = ctypes.windll.user32

    # Set the process DPI awareness to ensure accurate resolution retrieval
    user32.SetProcessDPIAware()

    # Get the width and height of the screen resolution
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    return width, height


def calculate_rectangle_area(width: int, height: int) -> int:
    """
    Calculates the area of a rectangle given its width and height.

    Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return width * height


# Get the screen resolution
width, height = get_screen_resolution()

# Calculate the area of the rectangle formed by the screen resolution
area = calculate_rectangle_area(width, height)

# Print the area
print(area)
