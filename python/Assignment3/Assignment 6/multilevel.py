# Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

class Puppy(Dog):  # Puppy inherits from Dog (and Animal indirectly)
    def whimper(self):
        print("Puppy whimpers")

# Test
puppy = Puppy()
puppy.speak()    # Inherited from Animal
puppy.bark()     # Inherited from Dog
puppy.whimper()  # Puppy-specific method
