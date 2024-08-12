class Product:
    def __init__(self, product_id, name, description, price, quantity=0):
        self.__id = product_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_price(self, price):
        if price >= 0:
            self.__price = price

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity

    # Methods to increase/decrease quantity
    def increase_quantity(self, amount):
        if amount > 0:
            self.__quantity += amount

    def decrease_quantity(self, amount):
        if 0 < amount <= self.__quantity:
            self.__quantity -= amount

    # String representation
    def __str__(self):
        return (f"Product: {self.__name}\n"
                f"Description: {self.__description}\n"
                f"Quantity: {self.__quantity}\n"
                f"Price: ${self.__price:.2f} each.\n")

# Testing the Product class
product1 = Product(1, "Pillow Set", "Set of two bamboo material pillows.", 45.99, 2)
product2 = Product(2, "Scented Candle", "Sandalwood, dual-wick candle.", 39.99, 4)

print(product1)
print(product2)
