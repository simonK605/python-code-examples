def read_image_list(image_list_file, label=None):
    """
    Read and return a list of image paths from the specified file.

    :param image_list_file: Path to the file containing a list of image paths.
    :param label: Optional label to be appended to each line in the file.
    :return: A list of image paths or None if there is an error.
    """
    try:
        with open(image_list_file, 'r') as file:
            lines = file.readlines()

            # Optionally append label to each line
            if label is not None:
                lines = [f'{line.strip()} {label}\n' for line in lines]

            return lines
    except FileNotFoundError:
        print(f"File '{image_list_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
image_list_file = 'path/to/your/image_list.txt'
label = '1'  # Optional label
image_paths = read_image_list(image_list_file, label)

if image_paths is not None:
    print("Image Paths:")
    for path in image_paths:
        print(path.strip())
