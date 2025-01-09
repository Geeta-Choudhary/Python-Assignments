'''
num1 = int(input('Enter number 1'))
num2 = int(input('Enter number2:'))

add=num1+num2
print(f'Addition of {num1}+{num2}={add}')

sub=num1-num2
print(f'Subtraction of {num1}-{num2}={sub}')

mul=num1*num2
print(f'Multiplication of {num1}X{num2}={mul}')

div=num1/num2
print(f'Division of {num1}/{num2}={div}')

floordiv=num1//num2
print(f'Floor Division of {num1//num2}={floordiv}')

pow=num1**num2
print(f'Power of {num1}^{num2}={pow}')

rem=num1%num2
print(f'Remainder of {num1%num2}={rem}')
'''

'''
class Calculator:
    def __init__(self):
        self.num1 =None
        self.num2 =None

    def calculation_details(self):
        self.num1 = int(input('Enter number1: '))
        self.num2 = int(input('Enter number2: '))
        return self.num1, self.num2

    def addition(self):
        return self.num1+self.num2
    def subtraction(self):
        return self.num1-self.num2
    def multiplication(self):
        return self.num1*self.num2
    def division(self):
        return self.num1/self.num2
    def floor_division(self):
        return self.num1//self.num2
    def power(self):
        return self.num1**self.num2
    def rem(self):
        return self.num1%self.num2

    def operation_result(self):
        print(f'ADDITION: {self.addition()}')
        print(f'SUBTRACTION: {self.subtraction()}')
        print(f'MULTIPLICATION: {self.multiplication()}')
        print(f'DIVISION: {self.division()}')
        print(f'FLOOR DIVISION: {self.floor_division()}')
        print(f'POWER: {self.power()}')
        print(f'REM: {self.rem()}')

if __name__ == '__main__':
    calculator = Calculator()
    calculator.calculation_details()
    calculator.operation_result()
'''
#using match-case

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number2: '))
while True :
    ch=int(input('Enter  your choice:\n 1.Addition \n 2.Subtraction \n 3.Multiplication '
          '\n 4.Division \n 5.FLOOR DIVISION \n 6.POWER \n 7.Remainder \n 8.Exit \n '))

    match ch:
        case 1:
            add=num1+num2
            print(f'Addition of {num1}+{num2}={add}')
        case 2:
            sub=num1-num2
            print(f'Subtraction of {num1}-{num2}={sub}')
        case 3:
            mul=num1*num2
            print(f'Multiplication of {num1}X{num2}={mul}')
        case 4:
            div=num1/num2
            print(f'Division of {num1}/{num2}={div}')
        case 5:
            floordiv=num1//num2
            print(f'Floor Division of {num1}//{num2}={floordiv}')
        case 6:
            pow=num1**num2
            print(f'Power of {num1}^{num2}={pow}')
        case 7:
            rem=num1%num2
            print(f'Remainder of {num1%num2}={rem}')
        case 8:
            print(f'')
            break
