def process_transactions(transactions_file: str) -> None:
    """
    Processes transactions from a CSV file.

    Parameters:
        transactions_file (str): The path to the CSV file containing transactions.

    Returns:
        None
    """
    # Open the transactions file in read mode
    with open(transactions_file, "r") as file:
        # Read all lines from the file
        lines = file.readlines()

    # Iterate through each line in the file (skipping the header)
    for i in range(1, len(lines)):
        # Split the line into individual transaction components
        transaction = lines[i].strip().split(",")

        # Extract transaction details
        buyer, seller, amount, date = transaction

        # Check if all required fields are present
        if buyer and seller and amount:
            print("Processing transaction:")
            print(f"Buyer: {buyer}, Seller: {seller}, Amount: {amount}, Date: {date}")
        else:
            print("Invalid transaction. Skipping...")

        # Calculate profit for the transaction
        calculate_profit(buyer, seller, float(amount))


def calculate_profit(buyer: str, seller: str, amount: float) -> None:
    """
    Calculates the profit for a transaction.

    Parameters:
        buyer (str): The buyer's name.
        seller (str): The seller's name.
        amount (float): The transaction amount.

    Returns:
        None
    """
    commission = 0.01  # Commission rate
    profit = amount - (amount * commission)
    print(f"Profit calculated for the transaction between {buyer} and {seller}: {profit}")


# Call the process_transactions function with the transactions CSV file
process_transactions("transactions.csv")
