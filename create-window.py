import tkinter as tk


def create_window(title: str, width: int, height: int) -> None:
    """
    Function to create a new window using Tkinter.

    Parameters:
        title (str): The title of the window.
        width (int): The width of the window.
        height (int): The height of the window.

    Returns:
        None
    """

    # Create a new Tkinter window
    window = tk.Tk()

    # Set the title of the window
    window.title(title)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position of the window to center it on the screen
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)

    # Set the geometry of the window (width x height + x_position + y_position)
    window.geometry(f"{width}x{height}+{position_right}+{position_top}")

    # Start the Tkinter event loop
    window.mainloop()
