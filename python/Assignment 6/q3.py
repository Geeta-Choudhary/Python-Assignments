class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
if __name__ == "__main__":
    # Create instances of Animal, Dog, and Cat
    generic_animal = Animal()
    dog = Dog()
    cat = Cat()

    # Demonstrate method overriding
    print("Animal:")
    generic_animal.speak()

    print("\nDog:")
    dog.speak()

    print("\nCat:")
    cat.speak()