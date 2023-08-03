def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime_numbers(numbers):
    prime_numbers = filter(is_prime, numbers)
    return list(prime_numbers)

# Testing the function
input_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
prime_numbers = filter_prime_numbers(input_numbers)
print(prime_numbers)  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
