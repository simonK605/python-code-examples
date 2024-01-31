import pandas as pd


def add_column_to_dataframe(data: dict, label: str, columns_to_sum):  # -> pd.DataFrame:
    """
    Add a new column to a DataFrame by summing values from specified columns.

    Args:
        data (dict): Dictionary containing column-wise data.
        label (str): Label for the new column to be added.
        columns_to_sum (list): List of column labels to be summed for the new column.

    Returns:
        pd.DataFrame: DataFrame with the new column added.
    """

    # Check if the provided DataFrame data is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Input 'data' should be a dictionary.")

    # Check if columns_to_sum is a list
    if not isinstance(columns_to_sum, list):
        raise ValueError("'columns_to_sum' should be a list of column labels.")

    # Check if all columns in columns_to_sum exist in the DataFrame
    if not set(columns_to_sum).issubset(data.keys()):
        missing_columns = set(columns_to_sum) - set(data.keys())
        raise ValueError(f"Columns {missing_columns} not found in the DataFrame.")

    # Create a DataFrame from the provided data
    df = pd.DataFrame(data)

    # Add a new column labeled 'label' by summing values from specified columns
    df[label] = df[columns_to_sum].sum(axis=1)

    return df


# Example usage
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}

# Add a new column 'C' by summing values from columns 'A' and 'B'
result_df = add_column_to_dataframe(data, 'C', ['A', 'B'])

# Display the resulting DataFrame
print(result_df)