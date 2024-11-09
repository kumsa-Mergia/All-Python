# Base class
class Product:
    def __init__(self, name, price):
        self._name = name  # protected attribute
        self._price = price  # protected attribute

    def get_details(self):
        return f"Product: {self._name}, Price: ${self._price:.2f}"

    def apply_discount(self, discount):
        self._price -= self._price * discount / 100

# Derived class
class Book(Product):
    def __init__(self, name, price, author, pages):
        super().__init__(name, price)  # calling the base class initializer
        self.author = author
        self.pages = pages

    # Overriding the get_details method (polymorphism)
    def get_details(self):
        return f"Book: {self._name}, Author: {self.author}, Pages: {self.pages}, Price: ${self._price:.2f}"

# Create instances
product1 = Product("Generic Product", 20.0)
book1 = Book("Python Programming", 30.0, "John Doe", 250)

# Display details
print(product1.get_details())  # Product: Generic Product, Price: $20.00
print(book1.get_details())     # Book: Python Programming, Author: John Doe, Pages: 250, Price: $30.00

# Apply discount
product1.apply_discount(10)
book1.apply_discount(15)

# Display updated details
print(product1.get_details())  # Product: Generic Product, Price: $18.00
print(book1.get_details())     # Book: Python Programming, Author: John Doe, Pages: 250, Price: $25.50
