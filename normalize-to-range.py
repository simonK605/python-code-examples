from typing import List

import numpy as np


def normalize_to_range(input_list: List[float], spec_range: tuple = (0, 1)) -> List[float]:
    """
    Normalizes the values in a list to a specified range.

    Parameters:
        input_list (List[float]): A list of floating-point numbers to be normalized.
        spec_range (tuple): A tuple specifying the target range for normalization.
            Default is (0, 1).

    Returns:
        List[float]: A list containing the normalized values within the specified range.
    """
    # Convert the input list to a NumPy array for easy manipulation
    array_input = np.array(input_list)

    # Calculate the minimum and maximum values from the input list
    min_val = array_input.min()
    max_val = array_input.max()

    # Normalize the input values to the range [0, 1]
    normalized_input = (array_input - min_val) / (max_val - min_val)

    # Extract the target range from the spec_range tuple
    spec_min, spec_max = spec_range

    # Scale the normalized values to the specified range
    normalized_to_spec = normalized_input * (spec_max - spec_min) + spec_min

    # Convert the normalized values back to a list and return
    return normalized_to_spec.tolist()
