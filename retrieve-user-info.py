def retrieve_user_info() -> tuple:
    """
    Retrieves user information from input.

    Returns:
        tuple: A tuple containing the user's name and age.
    """
    # Prompt the user to enter their name and age separated by comma
    print("Please enter your name and age separated by comma (e.g., John,25): ")

    # Read user input
    user_input = input()

    # Split the user input into name and age
    user_data = user_input.split(",")
    name = user_data[0].strip()  # Extract the name and remove leading/trailing spaces
    age = user_data[1].strip()  # Extract the age and remove leading/trailing spaces

    return name, age


def process_user_data() -> None:
    """
    Processes user data by retrieving user information and displaying it.

    Returns:
        None
    """
    # Retrieve user information
    name, age = retrieve_user_info()

    # Check if name or age is empty
    if not name or not age:
        print("Invalid input")  # Print error message if name or age is empty
        return

    # Print user information
    print(f"Hello {name}, your age is {age}")


# Call the process_user_data function to start the program
process_user_data()
