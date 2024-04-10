def extract_keys(dictionary):
    """
    Extract all keys from a dictionary.

    Parameters:
    - dictionary (dict): The dictionary from which keys will be extracted.

    Returns:
    list: A list containing all keys from the dictionary.
    """
    keys_list = list(dictionary.keys())
    return keys_list


# Example usage
example_dict = {'a': 1, 'b': 2, 'c': 3}
keys_result = extract_keys(example_dict)
print(keys_result)
