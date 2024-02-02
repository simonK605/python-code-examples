import matplotlib.pyplot as plt
import pandas as pd


def plot_histogram(data_series: pd.Series, bins: int = 10):
    """
    Plots a histogram of a numerical data series using Matplotlib.

    This function takes a Pandas Series containing numerical data and generates
    a histogram using Matplotlib. Users can customize the number of bins in the
    histogram.

    Parameters:
    - data_series (pd.Series): Pandas Series containing numerical data.
    - bins (int, optional): Number of bins for the histogram. Defaults to 10.

    Returns:
    None
    """
    # Plot the histogram with specified bins and edge color
    plt.hist(data_series, bins=bins, edgecolor='black')

    # Set title and labels for the axes
    plt.title('Histogram of Numerical Data Series')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Display the histogram
    plt.show()
