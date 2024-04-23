def is_connected(graph):
    """
    Check if a graph represented by an adjacency list is connected.

    Args:
    graph (dict): An adjacency list representing the graph.

    Returns:
    bool: True if the graph is connected, False otherwise.
    """
    def dfs(node, visited):
        """
        Depth-first search to traverse the graph and mark visited nodes.

        Args:
        node: The current node being visited.
        visited (set): A set to store visited nodes.

        Returns:
        None
        """
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    if not graph:
        return True  # An empty graph is considered connected

    start_node = next(iter(graph))
    visited_nodes = set()
    dfs(start_node, visited_nodes)

    return len(visited_nodes) == len(graph)


# Example usage:
# Define the graph as an adjacency list (dictionary)
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

result = is_connected(graph_example)
print(result)
