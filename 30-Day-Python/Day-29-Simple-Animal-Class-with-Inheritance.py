# Define the base class Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return f"{self.name} is a {self.species}"

# Define a Dog class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class constructor
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"{self.name} is a {self.breed} dog."

# Define a Cat class that inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the parent class constructor
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

    def __str__(self):
        return f"{self.name} is a {self.color} cat."

# Create instances of Dog and Cat
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Black")

# Print out their details and make them speak
print(dog1)
print(dog1.speak())

print(cat1)
print(cat1.speak())
