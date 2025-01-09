def fibonacci_recursive(n):
    # Base cases
    if n <= 1:
        return n
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_series(num_terms):
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci series:")
        for i in range(num_terms):
            print(fibonacci_recursive(i), end=" ")

if __name__ == "__main__":
    # Get user input for the number of terms
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    print_fibonacci_series(num_terms)
