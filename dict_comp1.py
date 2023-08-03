keys = ["name", "age", "country", "language"]
values = ["Alice", 25, "USA", "English"]

result_dict = {key: value for key, value in zip(keys, values)}

print(result_dict)
