'''
class Rectangle:
    def __init__(self):
        self.width=None
        self.length=None

    def inputs(self):
        self.width = int(input('Enter Width: '))
        self.length = int(input('Enter Length: '))
        return self.width,self.length

    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*(self.width+self.length)
    def result(self):
        print(f'Area of Rectangle: {self.area()}')
        print(f'Perimeter of Rectangle: {self.perimeter()}')

if __name__=='__main__':
    Area=Rectangle()
    Area.inputs()
    Area.result()
'''

'''
print(f'Code of area & perimeter of Rectangle')
width = int(input('Enter Width: '))
length = int(input('Enter Length: '))
area=width*length
print(f'Area :{area}')
perimeter=2*(width+length)
print(f'Perimeter:{perimeter}')
'''

def rectangle():
    width = int(input('Enter Width: '))
    length = int(input('Enter Length: '))
    area = width * length
    perimeter = 2 * (width + length)
    return area,perimeter

if __name__ == '__main__':
    area,perimeter=rectangle()
    print(f'Area :{area}')
    print(f'Perimeter:{perimeter}')