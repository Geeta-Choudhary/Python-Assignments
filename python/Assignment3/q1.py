import math


def area_circle(radius):
    return math.pi * radius**2

def square(*args):
    print("squares of variable arguments")
    for i in args:
        print(i * i)

def add(*args):
    print("for printing the sum of all variable no.of argument ")
    res=0
    for i in args:
        res=res+i
    print(res)


def add2(a,*args):
    print("for adding arguments with 1 constant argument")
    for i in args:
        print(a+i)

if __name__ == '__main__':
    print(area_circle(3))
    square(1,2,3,4)
    print()
    add(2,2,2)
    print()
    add2(2,10,20,30)
