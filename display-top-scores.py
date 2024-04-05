def display_top_scores(scores):
    """
    Displays the top three scores from a list of scores.

    Args:
    scores (list): A list of integers representing scores.

    Returns:
    None
    """
    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)

    # Take the top three scores (or less if there are fewer than three scores)
    top_three_scores = sorted_scores[:3]

    # Display the top three scores
    print("Top Three Scores:")
    for i, score in enumerate(top_three_scores, start=1):
        print(f"{i}. {score}")


# Example usage:
scores_list = [85, 92, 78, 95, 88, 90, 87]
display_top_scores(scores_list)
