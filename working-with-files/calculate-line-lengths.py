def calculate_line_lengths(file_path):
    """
    Calculate the lengths of each line in a text file.

    Parameters:
    - file_path (str): The path to the text file.

    Returns:
    - list: A list containing the lengths of each line in the file.
    """
    with open(file_path, 'r') as file:
        line_lengths = []
        for line in file:
            length = len(line.strip())
            line_lengths.append(length)
        return line_lengths


def main():
    """
    Main function to demonstrate calculating line lengths from a text file.
    """
    text_file_path = 'sample.txt'
    try:
        line_lengths = calculate_line_lengths(text_file_path)
        print(f"Line lengths: {line_lengths}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
