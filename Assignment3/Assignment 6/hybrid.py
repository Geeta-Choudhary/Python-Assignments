# Hybrid Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal:
    def walk(self):
        print("Mammal walks")

class Dog(Animal, Mammal):  # Dog inherits from both Animal and Mammal
    def bark(self):
        print("Dog barks")

class Puppy(Dog):  # Puppy inherits from Dog (and Animal, Mammal indirectly)
    def whimper(self):
        print("Puppy whimpers")

# Test
puppy = Puppy()
puppy.speak()    # Inherited from Animal
puppy.walk()     # Inherited from Mammal
puppy.bark()     # Inherited from Dog
puppy.whimper()  # Puppy-specific method
