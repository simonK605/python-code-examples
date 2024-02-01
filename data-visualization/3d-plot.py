import numpy as np
import matplotlib.pyplot as plt


def create_3d_plot():
    """
    Creates a 3D plot using Numpy and Matplotlib.

    This function generates a simple 3D plot with sample data using Numpy and Matplotlib.
    The plot displays a curve in 3D space.

    Parameters:
    None

    Returns:
    None
    """
    # Create a new figure and a 3D subplot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Example data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)

    # Plot the curve in 3D space
    ax.plot(x, y, z)

    # Set labels and title for the plot
    ax.set_title('3D Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Display the plot
    plt.show()
