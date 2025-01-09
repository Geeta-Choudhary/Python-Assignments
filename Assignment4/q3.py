def process_employee_data(employee_data):
    first_name,last_name,age,role,city=employee_data
    # Print the unpacked variables
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Age: {age}")
    print(f"Role: {role}")
    print(f"Location: {city}")

    if 'Developer' in employee_data:
        print("developer is present")
    else:
        print("developer is not present")

    emp_list=list(employee_data)
    emp_list.append("Full-time")
    print("Modified Employee List:", emp_list)

#Testing the function with the given tuple
employee_data = ('John', 'Doe', 34, 'Developer', 'New York')
print(employee_data)
process_employee_data(employee_data)
