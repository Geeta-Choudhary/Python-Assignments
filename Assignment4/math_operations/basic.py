'''
def get_numbers():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    return number1, number2
'''

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def operation_results(a, b):
    print(f"Addition: {addition(a, b)}")
    print(f"Subtraction: {subtraction(a, b)}")
    print(f"Multiplication: {multiplication(a, b)}")
    print(f"Division: {division(a, b)}")

if __name__ == "__main__":
    #num1, num2 = get_numbers()
    operation_results(10,2)
