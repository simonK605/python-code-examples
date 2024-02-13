import hashlib

# Path to the file for which we want to calculate the SHA-256 hash
file_path = "test.txt"


def get_file_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.

    Parameters:
    - file_path (str): The path to the file for which the hash is calculated.

    Returns:
    str: The SHA-256 hash in hexadecimal format.
    """
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode
    with open(file_path, "rb") as file:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()


# Example usage
print(get_file_hash(file_path))
