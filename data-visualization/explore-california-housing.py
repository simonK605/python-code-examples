from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def explore_california_housing():
    """
    Function to explore the California housing dataset.
    Fetches the dataset, prints description, feature names, data shape, and target shape.
    Visualizes data distribution and correlation matrix.
    """
    # Fetch the California housing dataset
    california_housing = fetch_california_housing()

    # Print dataset description, feature names, data shape, and target shape
    print("Dataset Description:")
    print(california_housing.DESCR)
    print("\nFeature Names:")
    print(california_housing.feature_names)
    print("\nData Shape:")
    print(california_housing.data.shape)
    print("\nTarget Shape:")
    print(california_housing.target.shape)

    # Visualize data distribution
    visualize_data_distribution(california_housing.data)


def visualize_data_distribution(data):
    """
    Function to visualize data distribution using pairplot.
    :param data: The dataset to visualize
    """
    # Set seaborn style and create pairplot for data visualization
    sns.set(style="ticks")
    sns.pairplot(pd.DataFrame(data, columns=fetch_california_housing().feature_names))
    plt.show()


def calculate_and_visualize_correlation_matrix(data):
    """
    Function to calculate and visualize correlation matrix.
    :param data: The dataset to calculate correlation matrix
    """
    # Calculate correlation matrix using Pandas DataFrame
    correlation_matrix = pd.DataFrame(data).corr()

    # Visualize correlation matrix using heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()


# Call the main function to explore the California housing dataset
explore_california_housing()
