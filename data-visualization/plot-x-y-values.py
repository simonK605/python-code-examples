import matplotlib.pyplot as plt


def plot_x_y_values(x_values: list, y_values: list, xlabel: str, ylabel: str, title: str) -> None:
    plt.plot(x_values, y_values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()


plot_x_y_values(
    x_values=[1, 2, 3, 4, 5],
    y_values=[1, 4, 9, 16, 25],
    xlabel="x-axis",
    ylabel="y-axis",
    title="My First Plot")

