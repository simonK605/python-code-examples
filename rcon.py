import os
import random

# Generate a 2D list of random integers representing an RCON matrix.
def generate_rcon(size, rows):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(rows)]

# Read RCON values from a file or generate them if the file does not exist.
def read_or_generate_rcon(size, rows, file_path=None):
    # Default file path if not provided
    if file_path is None:
        file_path = os.getenv("RCON_FILE_PATH", "rcon.txt")

    try:
        if os.path.exists(file_path):
            # If the file exists, read RCON values from the file
            with open(file_path, 'r') as file:
                rcon_values = [[int(value) for value in line.split()] for line in file]
        else:
            # If the file does not exist, generate RCON values
            rcon_values = generate_rcon(size, rows)

            # Save generated values to the file
            with open(file_path, 'w') as file:
                for row in rcon_values:
                    # Write each row as space-separated values
                    file.write(" ".join(map(str, row)) + "\n")

        return rcon_values
    except Exception as e:
        # Handle exceptions and print an error message
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the file if it is open
        if 'file' in locals() and not file.closed:
            file.close()

# Example usage
rcon_values = read_or_generate_rcon(size=4, rows=3)
if rcon_values is not None:
    print("Generated or read RCON values:")
    print(rcon_values)
else:
    print("Failed to read or generate RCON values.")