def body_mass_index():
    weight = float(input('Enter weight in kg :'))
    height = float(input('Enter height in meters :'))
    bmi=weight/(height ** 2)

    if (bmi >= 25) & (bmi<=29.9):
        print(f'Your BMI is {bmi:.2f},your are overweight with weight [{weight}]')
    elif bmi<18.5:
        print(f'Your BMI is {bmi:.2f},your underweight with weight [{weight}]')
    elif (bmi>=18.5) & (bmi<=24.9):
        print(f'Your BMI is {bmi:.2f},your normal with weight[{weight}]')
    else:
        print(f'Your BMI is {bmi:.2f},YOur obese with weight[{weight}]')
if __name__=='__main__':
    body_mass_index()