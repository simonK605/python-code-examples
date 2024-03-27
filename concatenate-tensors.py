import torch


def concatenate_tensors(tensors: list, dimension: int):
    """
    Concatenate a list of tensors along a specified dimension.

    Args:
        tensors (list): List of tensors to concatenate.
        dimension (int): Dimension along which to concatenate the tensors.

    Returns:
        torch.Tensor: The concatenated tensor.
    """
    # Concatenate the tensors along the first dimension
    concatenated = torch.cat(tensors, dim=dimension)

    return concatenated


# Example tensors
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.tensor([[7, 8, 9], [10, 11, 12]])

# Concatenate along dimension 0 (rows)
result = concatenate_tensors([tensor1, tensor2], 0)

# Print the result
print(result)
