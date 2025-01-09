class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f"1. Brand: {self.brand}\n2. Speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, milege):
        super().__init__(brand, speed)
        self.milege = milege

    def show_details(self):  # Fix indentation here
        super().show_details()
        print(f"3. Mileage: {self.milege} km/l")


if __name__ == "__main__":
    # Create a Vehicle object
    vehicle = Vehicle("Toyota", 120)
    print("Vehicle Details:")
    vehicle.show_details()

    print("\nCar Details:")
    # Create a Car object
    car = Car( "Toyota", 120,18)
    car.show_details()

