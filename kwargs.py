from typing import Dict

def calculate_total_cost(**kwargs: Dict[str, float]) -> float:
    """
    Calculate the total cost of items using their prices.
    
    This function takes a dictionary of items and their corresponding prices
    and returns the total cost by summing up the prices.
    
    Parameters:
    **kwargs (dict): A dictionary where keys are item names and values are item prices.
    
    Returns:
    float: The total cost calculated from the input item prices.
    """
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
