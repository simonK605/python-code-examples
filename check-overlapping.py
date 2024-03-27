def overlapping(list1, list2):
    """
    Check if there is any overlap between two lists or between a list and a string representation of a list.

    Parameters:
    list1 (list or str): The first list or string representation of a list.
    list2 (list or str): The second list or string representation of a list.

    Returns:
    bool: True if there is an overlap, False otherwise.
    """

    # Convert list1 to a list if it's a string
    if isinstance(list1, str):
        try:
            list1 = [int(num.strip()) for num in list1.split(',')]  # Convert string to list of integers
        except ValueError:
            print("Error: Could not convert string to list")  # Handle conversion error
            return False

    # Convert list2 to a list if it's a string
    if isinstance(list2, str):
        try:
            list2 = [int(num.strip()) for num in list2.split(',')]  # Convert string to list of integers
        except ValueError:
            print("Error: Could not convert string to list")  # Handle conversion error
            return False

    # Check if both inputs are lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        print("Both list1 and list2 must be lists")  # Notify if inputs are not lists
        return False

    # Check for overlapping elements
    for item in list1:
        if item in list2:  # Check if item in list1 exists in list2
            return True  # Return True if overlap found
    return False  # Return False if no overlap found


# Example usage
list1 = [1, 2, 3, 4, 5, 6]
list2 = "6, 7, 8, 9"
if overlapping(list1, list2):
    print("overlapping")
else:
    print("not overlapping")
