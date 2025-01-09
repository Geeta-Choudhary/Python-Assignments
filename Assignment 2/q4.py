def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test the function with different sets of keyword arguments
print("Test 1:")
print_details(name="Alice", age=25, city="New York")

print("\nTest 2:")
print_details(product="Laptop", brand="Dell", price=799)

print("\nTest 3:")
print_details(course="Python Programming", duration="3 months", instructor="John Doe" , school="kilbil")




'''
def print_details(name="geeta",sal=9000,age=12):
    return name,sal,age

print(print_details(name='meera',sal=2300))
print(print_details(age=90,name='Jack',sal=2000))
print(print_details('John',8900,56))
print(print_details())
print(print_details('Joy',27000))
'''