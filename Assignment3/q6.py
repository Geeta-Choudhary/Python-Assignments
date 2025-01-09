def round_to_one(numbers):
    # Use map with round() to round each number to 1 decimal place
     result=(map(lambda x: round(x, 1), numbers))
     print(list(result))

# Example usage
round_to_one([3.14159, 2.71828, 1.61803])

