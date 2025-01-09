def fibonacci(n):
    '''THis function prints the n^th fibonacci term'''
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def print_fibonacci_series(n):
    ''' Print the Fibonacci series up to the 5th term '''
    for i in range(n):
        print(i,end=" ")


print(fibonacci.__doc__)
print(f"fibonacci{[6]}^th term: {fibonacci(6)}")
print(print_fibonacci_series.__doc__)
print_fibonacci_series(6)


print()


#This approach is efficient for printing a Fibonacci series without using recursion,
#which can be slow for larger sequences due to repeated calculations.


def fibonacci_series(n):
    '''Print the Fibonacci series up to the 5th term  without recursive'''
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
print(fibonacci_series.__doc__)
fibonacci_series(6)

print()
