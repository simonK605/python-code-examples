import json


def parse_json_file(file_path):
    """
    Parse a JSON file using the json library.

    Parameters:
    - file_path (str): The path to the JSON file to be parsed.

    Returns:
    dict: Parsed JSON content as a Python dictionary.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            # Use the json library to load the JSON content
            data = json.load(json_file)

        return data

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


# Example usage
json_file_path = 'your_json_file.json'  # Replace with the actual path to your JSON file
parsed_json = parse_json_file(json_file_path)

if parsed_json:
    # Now you can use 'parsed_json' as a Python dictionary to access the data
    print(parsed_json)
