'''
def area_of_rectangle():
    length=float(input("Enter the length of the rectangle: "))
    width=float(input("Enter the width of the rectangle: "))
    print("The area of the rectangle is:",length*width)

if __name__=='__main__':
    area_of_rectangle()
'''
def area_of_rectangle(length, width):
    """Calculate and return the area of a rectangle."""
    return(length * width)

# Testing the function with different values
print("Test Case 1: Length = 5, Width = 3")
print("Expected Output: 15")
print("Actual Output:",area_of_rectangle(5, 3))


print("Test Case 2: Length = 7.5, Width = 4.2")
print("Expected Output: 31.5")
print("Actual Output:", area_of_rectangle(7.5, 4.2))
print()

print("Test Case 3: Length = 0, Width = 10")
print("Expected Output: 0")
print("Actual Output:", area_of_rectangle(0, 10))
print()

print("Test Case 4: Length = 10, Width = 10")
print("Expected Output: 100")
print("Actual Output:", area_of_rectangle(10, 10))
print()
