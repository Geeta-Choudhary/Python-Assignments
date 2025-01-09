
def user_details():
   name = input('Enter your name: ')
   age = int(input('Enter your age: '))
   print(f'HELLO,[{name}]! You are [{age}] years old')
   #return name,age


if __name__ == '__main__':
    user_details()
'''

class User:
    def __init__(self):
        self.name =None
        self.age =None

    def user_details(self):
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))
        print(f'HELLO, [{name}]! You are [{age}] years old')
        return self.name, self.age

if __name__ == '__main__':
    user = User()
    user.user_details()
'''

