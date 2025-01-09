def number():
    num1 = int(input('Enter number1 :'))
    num2 = int(input('Enter number2 :'))

    if num1 >num2:
        print(f'Number [{num1}] is Greater than [{num2}]')
    elif num1 == num2:
        print(f'Number [{num1}] is equal to [{num2}]')
    else:
        print(f'Number [{num1}] is Less than [{num2}]')

if __name__=='__main__':
    number()