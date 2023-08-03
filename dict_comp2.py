# Create a dictionary named original_scores
original_scores = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 88,
    "David": 95,
    "Eve": 62
}

# Create a new dictionary high_scores using a dictionary comprehension
# The comprehension filters students with scores greater than 80
high_scores = {student: score for student, score in original_scores.items() if score > 80}

# Print the resulting high_scores dictionary
print(high_scores)
