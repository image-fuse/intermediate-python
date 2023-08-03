def calculate_total_cost(**kwargs):
    total_cost = sum(kwargs.values())
    return total_cost

# Testing the function
items = {
    'item1': 10.99,
    'item2': 5.49,
    'item3': 7.25,
}

total_cost = calculate_total_cost(**items)
print(f"Total cost: ${total_cost:.2f}")
