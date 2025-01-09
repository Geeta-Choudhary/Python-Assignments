class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def display_details(self):
        print(f"Employee Name:{self.name} \n Position:{self.position} \n salary:{self.salary}")


emp1 = Employee("Alice Johnson", "Software Engineer", 95000)
emp1.display_details()
