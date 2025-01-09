def calculate_simple_interest():
    # Get user input for principal, rate of interest, and time period
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))

    # Calculate the simple interest
    simple_interest = (principal * rate * time) / 100

    # Display the result
    print(f"The calculated simple interest is: {simple_interest:.2f}")

if __name__ == "__main__":
    calculate_simple_interest()
