class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower

    def show_engine_details(self):
        print(f"Horsepower: {self.horsepower} HP")

class Body:
    def __init__(self,material):
        self.material=material

    def show_body_details(self):
        print(f"Body Material: {self.material}")

class Car(Engine,Body):
    def __init__(self,horsepower,material):
        Engine.__init__(self, horsepower)
        Body.__init__(self, material)

    def show_car_details(self):
        print("Car Details:")
        self.show_engine_details()
        self.show_body_details()

if __name__ == "__main__":
    # Create a Car object
    car = Car(250, "Aluminum")
    car.show_car_details()

