import matplotlib.pyplot as plt


def plot_line_graph(x_values, y_values):
    """
    Draws a simple line graph using Matplotlib.

    This function takes two lists of values (x_values and y_values) and creates
    a line graph using Matplotlib. The graph includes a title, X-axis label, and
    Y-axis label.

    Parameters:
    - x_values (list): List of values for the X-axis.
    - y_values (list): List of values for the Y-axis.

    Returns:
    None
    """
    # Plot the line graph
    plt.plot(x_values, y_values)

    # Set title and labels for the axes
    plt.title('Line Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Display the graph
    plt.show()
