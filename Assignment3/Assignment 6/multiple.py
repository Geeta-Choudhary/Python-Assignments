# Multiple Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal:
    def walk(self):
        print("Mammal walks")

class Dog(Animal, Mammal):  # Dog inherits from both Animal and Mammal
    def bark(self):
        print("Dog barks")

# Test
dog = Dog()
dog.speak()  # Inherited from Animal
dog.walk()   # Inherited from Mammal
dog.bark()   # Dog's own method
