import csv


def parse_csv_file(file_path):
    """
    Parses a CSV file and returns its content as a list of lists.

    Parameters:
    - file_path (str): The path to the CSV file to be parsed.

    Returns:
    list: A list containing each row of the CSV file as a sub-list.
    """

    # Create an empty list to store the parsed data
    data = []

    # Open the CSV file with the specified file path in binary mode
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append each row to the 'data' list
            data.append(row)

    # Return the parsed data
    return data


# Example usage
csv_file_path = 'your_csv_file.csv'  # Replace with the actual path to your CSV file
parsed_data = parse_csv_file(csv_file_path)

# Print the parsed data to the console
print(parsed_data)
