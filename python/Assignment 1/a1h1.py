def temperature_conversion():
    temp=float(input("Enter the temperature value: "))
    unit=input("Enter the unit").strip().lower()

    if unit== 'celsius':
        fahrenheit = (temp * 9 / 5) + 32
        print(f"{temp} Celsius is equal to {fahrenheit} Fahrenheit.")

    elif unit == 'fahrenheit':
        celsius = (temp - 32) * 5 / 9
        print(f"{temp} Fahrenheit is equal to {celsius} Celsius.")
    else:
        print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")


if __name__=='__main__':
    temperature_conversion()