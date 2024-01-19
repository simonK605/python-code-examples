import os
import random

def generate_rcon(size, rows):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(rows)]

def read_or_generate_rcon(size, rows):
    file_path = "rcon.txt"

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
                file.write(" ".join(map(str, row)) + "\n")

    return rcon_values

# Example usage
rcon_values = read_or_generate_rcon(size=4, rows=3)
print(rcon_values)