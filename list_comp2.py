# Input lists
list1 = [2, 3, 4, 5]
list2 = [10, 20, 30, 40]

# Create a list containing the product of corresponding elements from both lists
product_list = [x * y for x, y in zip(list1, list2)]

# Print the resulting product list
print(product_list)
