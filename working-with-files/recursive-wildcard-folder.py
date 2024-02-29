import glob

# Define the base directory and the file pattern you want to search for
base_directory = '/path/to/your/base/directory'
file_pattern = '*.txt'  # Adjust the pattern as needed

# Use the glob.glob method with the recursive wildcard **
file_list = glob.glob(f'{base_directory}/**/{file_pattern}', recursive=True)

# Print the list of matching files
print("Matching Files:")
for file_path in file_list:
    print(file_path)