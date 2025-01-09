import q4
#from q4 import factorial

def calculate_factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    result = q4.factorial(num)
    #result = factorial(num)
    print(f"The factorial of {num} is {result}")
# Call the function
calculate_factorial()