def tuples_to_lists(tuples):
    """
    Convert a list of tuples to a list of lists.

    Args:
    tuples (list): List of tuples.

    Returns:
    list: List of lists.
    """
    # Convert the tuples to lists
    lists = [list(tup) for tup in tuples]
    return lists


tuples = [(1, 2), (3, 4), (5, 6)]

print(tuples_to_lists(tuples))
