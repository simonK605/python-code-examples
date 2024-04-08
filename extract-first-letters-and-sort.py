def extract_first_letters_and_sort(word_list):
    """
    Extracts the first letter of each word in the given list and sorts them alphabetically.

    Parameters:
        word_list (list): A list of words.

    Returns:
        list: A sorted list containing the first letters of the words.
    """
    first_letters = []

    # Iterate through each word in the list
    for word in word_list:
        # Add the first letter of the word to the list
        first_letters.append(word[0])

    # Sort the list of first letters alphabetically
    first_letters.sort()

    return first_letters


def main() -> None:
    """
    Main function to demonstrate the usage of extract_first_letters_and_sort function.
    """
    # Sample list of words
    words = ["apple", "banana", "cherry", "", "elderberry"]

    # Extract and sort the first letters of the words
    results = extract_first_letters_and_sort(words)

    # Print the sorted first letters
    for letter in results:
        print(letter)


if __name__ == "__main__":
    main()
