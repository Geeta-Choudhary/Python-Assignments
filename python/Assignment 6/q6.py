# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

# Test
dog = Dog()
dog.speak()  # Inherited method
dog.bark()   # Derived class method
