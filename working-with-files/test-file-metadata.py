import os
import time


def test_file_metadata(file_path):
    """
    Retrieve and print metadata information of a file.

    Parameters:
        file_path (str): The path to the file for which metadata needs to be retrieved.

    Returns:
        None
    """
    # Retrieve file metadata using os.stat
    stat_info = os.stat(file_path)

    # Access and format file metadata
    creation_time = time.ctime(stat_info.st_ctime)

    # Print the creation time of the file
    print(f"Creation time: {creation_time}")


# Example usage
if __name__ == "__main__":
    # Provide the path to the file you want to test
    file_path_to_test = "/path/to/your/file.txt"

    # Call the function with the file path
    test_file_metadata(file_path_to_test)