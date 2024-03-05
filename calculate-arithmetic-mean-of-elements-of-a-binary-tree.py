class TreeNode:
    def __init__(self, value):
        """
        TreeNode class represents a node in a binary tree.

        Parameters:
        - value: The value associated with the node.
        """
        self.value = value
        self.left = None
        self.right = None


def tree_arithmetic_mean(node):
    """
    Calculate the arithmetic mean of all elements in a binary tree.

    Parameters:
    - node: The root node of the binary tree.

    Returns:
    A tuple (sum, count), where:
    - sum: The sum of all values in the tree.
    - count: The total number of nodes in the tree.
    """
    # Base case: empty tree
    if not node:
        return 0, 0  # return 0 for both sum and number of nodes

    # Recursive calls
    left_sum, left_count = tree_arithmetic_mean(node.left)
    right_sum, right_count = tree_arithmetic_mean(node.right)

    # Combine results
    total_sum = left_sum + right_sum + node.value
    total_count = left_count + right_count + 1

    # Calculate and return mean
    return total_sum, total_count


# Create a sample binary tree
binary_tree = TreeNode(5)
binary_tree.left = TreeNode(3)
binary_tree.right = TreeNode(7)
binary_tree.left.left = TreeNode(2)
binary_tree.left.right = TreeNode(4)
binary_tree.right.right = TreeNode(8)

# Calculate the mean
total_sum, total_count = tree_arithmetic_mean(binary_tree)
mean = total_sum / total_count

# Print the result
print(f"Mean of all elements: {mean}")
