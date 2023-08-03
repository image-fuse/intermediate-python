original_scores = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 88,
    "David": 95,
    "Eve": 62
}

high_scores = {student: score for student, score in original_scores.items() if score > 80}

print(high_scores)
