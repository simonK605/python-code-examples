class MyStringManipulator:
    def __init__(self, my_string: str) -> None:
        """
        Initializes an instance of MyStringManipulator with a given string.

        Parameters:
            my_string (str): The string to be manipulated.
        """
        self.my_string = my_string

    def split_string(self, delimiter: str) -> list:
        """
        Splits the string using the specified delimiter.

        Parameters:
            delimiter (str): The delimiter used to split the string.

        Returns:
            list: A list of words obtained after splitting the string.
        """
        word_list = self.my_string.split(delimiter)
        return word_list

    def first_word_length(self) -> int:
        """
        Calculates the length of the first word in the string.

        Returns:
            int: The length of the first word.
        """
        word_list = self.split_string(" ")
        first_word_length = len(word_list[0])
        return first_word_length


def process_string(manipulator: MyStringManipulator) -> None:
    """
    Processes a string manipulator object and prints the length of the first word.

    Parameters:
        manipulator (MyStringManipulator): An instance of MyStringManipulator.

    Returns:
        None
    """
    str_length = manipulator.first_word_length()
    print(f"First word length: {str_length}")


if __name__ == "__main__":
    # Define the input string
    input_string = "0 , World!"

    # Create an instance of MyStringManipulator
    my_manipulator = MyStringManipulator(input_string)

    # Process the string and print the length of the first word
    process_string(my_manipulator)
