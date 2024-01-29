import os
from typing import Dict


def aggregate_file_info_by_extension(directory_path: str) -> Dict[str, Dict[str, int]]:
    """
    Aggregate file information by extension in the specified directory.

    Args:
        directory_path (str): The path to the directory for which file information needs to be aggregated.

    Returns:
        dict: A dictionary containing aggregated file information by extension.
              The keys are file extensions, and the values are dictionaries with 'count' and 'size_in_bytes'.

    Example:
        >>> result = aggregate_file_info_by_extension('/path/to/directory')
        >>> print(result)
        {'txt': {'count': 2, 'size_in_bytes': 1024},
         'jpg': {'count': 3, 'size_in_bytes': 2048},
         'py': {'count': 1, 'size_in_bytes': 512}}
    """
    # Initialize an empty dictionary to store file information by extension
    file_dict = {}

    # Traverse through the directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Construct the full path to the file
            file_path = os.path.join(root, file)

            # Get the size of the file in bytes
            size_in_bytes = os.path.getsize(file_path)

            # Extract the file extension
            file_extension = os.path.splitext(file)[1]

            # Update the file dictionary with file information
            if file_extension not in file_dict:
                file_dict[file_extension] = {"count": 1, "size_in_bytes": size_in_bytes}
            else:
                file_dict[file_extension]["count"] += 1
                file_dict[file_extension]["size_in_bytes"] += size_in_bytes

    return file_dict
