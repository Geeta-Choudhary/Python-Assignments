# Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

class Cat(Animal):  # Cat also inherits from Animal
    def meow(self):
        print("Cat meows")

# Test
dog = Dog()
cat = Cat()
dog.speak()  # Inherited from Animal
dog.bark()   # Dog's own method

cat.speak()  # Inherited from Animal
cat.meow()   # Cat's own method
