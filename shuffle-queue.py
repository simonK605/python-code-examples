from queue import Queue
import random


def shuffle_queue(q):
    """
    Shuffle the elements in a given queue.

    Parameters:
    - q (Queue): The queue containing elements to be shuffled.

    Returns:
    None: The function shuffles the elements in the input queue in-place.
    """
    # Empty the queue into a list
    lst = []
    while not q.empty():
        lst.append(q.get())

    # Shuffle the list
    random.shuffle(lst)

    # Put the shuffled elements back into the queue
    for item in lst:
        q.put(item)


# Example usage
my_queue = Queue()
# Assuming the queue has some elements already
# Add elements to the queue using my_queue.put(element)

shuffle_queue(my_queue)
