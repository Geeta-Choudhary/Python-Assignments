'''
num = int(input('Enter number :'))
if num % 2 == 0 :
    print(f'Number{num} is Even')
else:
    print(f'Number{num} is odd')
'''

'''
def even_odd():
    num = int(input('Enter number :'))
    if num < 0 :
        print(f'Enter the positive number.Number [{num}] is negative integer')
    elif num == 0:
        print(f'0 in neither even nor odd')
    elif num % 2 == 0:
        print(f'Number [{num}] is Even')
    else:
        print(f'Number [{num}] is odd')

if __name__=='__main__':
    even_odd()
'''

# Take integer input from the user
num = int(input("Enter an integer: "))

# Use a list comprehension to determine and print if the number is even or odd
[print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}.")]

