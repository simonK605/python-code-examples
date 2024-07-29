def process_orders(order_list):
    """
    Processes a list of orders.

    Parameters:
        order_list (list): A list of orders to be processed.

    Raises:
        ValueError: If the order list is empty.
    """
    # Check if the order list is empty
    if not order_list:
        raise ValueError("Order list must not be empty.")

    # Process each order in the order list
    for order in order_list:
        print(f"Processing order: {order}")


def get_last_order(customer_orders):
    """
    Retrieves the last order from a list of customer orders.

    Parameters:
        customer_orders (list): A list of customer orders.

    Returns:
        Any: The last order in the list.
    """
    # Get the last order from the list
    last_order = customer_orders[-1]
    return last_order


def print_last_order(customer_orders) -> None:
    """
    Prints the last order from a list of customer orders.

    Parameters:
        customer_orders (list): A list of customer orders.

    Returns:
        None
    """
    # Get the last order
    last_order = get_last_order(customer_orders)
    # Print the last order
    print(f"Last order: {last_order}")


if __name__ == "__main__":
    # Sample list of customer orders
    customer_orders = [5, 8, 99]

    print("Processing customer orders:")
    # Process the customer orders
    process_orders(customer_orders)

    print("Printing last order:")
    # Print the last order from the customer orders
    print_last_order(customer_orders)
