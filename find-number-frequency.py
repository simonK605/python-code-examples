from collections import Counter


def find_mode(numbers):
    """
    Finds the mode (most frequent element) in a list of numbers.

    Parameters:
        numbers (list): A list of numbers.

    Returns:
        int: The mode of the list.
    """
    # Count the frequency of each number using Counter
    number_frequency = Counter(numbers)

    # Sort the number frequency dictionary by frequency in descending order
    sorted_number_frequency = sorted(number_frequency.items(), key=lambda x: -x[1])

    # Get the most frequent number (mode)
    mode = sorted_number_frequency[0][0]

    return mode


def test_find_mode() -> None:
    """
    Function to test the find_mode function with sample data.
    """
    # Sample test data
    test_list1 = [1, 2, 3, 3, 3, 4, 4, 2, 2, 2, 2]
    test_list2 = [8, 8, 9, 9, 9]

    # Print the mode for each test list
    print(find_mode(test_list1))  # 2
    print(find_mode(test_list2))  # 9


# Call the test function to demonstrate the functionality
test_find_mode()
