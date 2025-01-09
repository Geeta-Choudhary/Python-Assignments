class Car:
    def __init__(self, brand, year,color=None):
        self.brand = brand
        self.year = year
        self.color = color


    def display_info(self):

        print(f"the car details \n brand:{self.brand} \n"
              f"year:{self.year}\n")
        if self.color:
              print(f" color:{self.color}")
c1=Car('honda',2014,'blue')
c1.display_info()