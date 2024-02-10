import gzip
import shutil


def decompress_gzip(input_file, output_file):
    """
    Decompresses a Gzip file.

    Parameters:
    - input_file (str): The path to the input Gzip file.
    - output_file (str): The path to the output file where the decompressed content will be saved.
    """
    # Open the Gzip file for reading
    with gzip.open(input_file, 'rb') as f_in:
        # Open the output file for writing
        with open(output_file, 'wb') as f_out:
            # Copy the contents from the Gzip file to the output file
            shutil.copyfileobj(f_in, f_out)


# Example usage
input_gzip_file = 'your_compressed_file.gz'  # Replace with the actual name of your Gzip file
output_file = 'output_file.txt'  # Specify the desired name for the decompressed output file

# Call the decompression function with the input and output file names
decompress_gzip(input_gzip_file, output_file)
