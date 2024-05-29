from typing import List, Any, Dict


def merge_lists_into_dict(keys: List[Any], values: List[Any]) -> Dict:
    """
    Merges two lists into a dictionary where the elements of the first list are used as keys
    and the elements of the second list are used as values.

    Parameters:
        keys (List[Any]): A list containing keys.
        values (List[Any]): A list containing values.

    Returns:
        Dict: A dictionary where keys are elements from the first list and values are elements from the second list.
    """
    # Use the zip function to pair corresponding elements from keys and values
    # Create a dictionary from the pairs using the dict constructor
    return dict(zip(keys, values))


# Example usage:
# Merge the lists ['s', 'd', 'f'] and ['ss', 'dd', 'ff'] into a dictionary
my_dict = merge_lists_into_dict(['s', 'd', 'f'], ['ss', 'dd', 'ff'])

# Print the resulting dictionary
print(my_dict)
