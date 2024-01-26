def calculate_average_exam_score(students_scores):
    total_score = 0
    for score in students_scores:
        total_score += score
    average_score = total_score / len(students_scores)
    return average_score


students_scores_math = [75, 90, 86, 92, 88]
students_scores_english = [8, 10]

print("Average Math Score:", calculate_average_exam_score(students_scores_math))  # Average Math Score: 86.2
print("Average English Score:", calculate_average_exam_score(students_scores_english))  # Average English Score: 9.0