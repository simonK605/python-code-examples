def replace_item(lst, current_item, new_item):
    """
    Replace occurrences of a specified item in a list with a new item.

    Parameters:
    - lst (list): The input list to be modified.
    - current_item: The item to be replaced in the list.
    - new_item: The item that will replace occurrences of the current_item.

    Returns:
    None: The function modifies the input list in-place and does not return a new list.
    """
    for i in range(len(lst)):
        if lst[i] == current_item:
            lst[i] = new_item


# Example usage
items = ["apple", "banana", "cherry"]
replace_item(items, "banana", "orange")
print(items)
