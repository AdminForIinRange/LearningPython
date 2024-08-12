class Store:
    def __init__(self, name, money=0.0):
        self.__name = name
        self.__money = money
        self.__products = []

    # Add a product to the store
    def order_product(self, product, amount):
        found_product = self.find_product(product.get_id())
        if found_product:
            found_product.increase_quantity(amount)
        else:
            product.increase_quantity(amount)
            self.__products.append(product)

    # Sell a product from the store
    def sell_product(self, product_id, amount):
        product = self.find_product(product_id)
        if product:
            if product.get_quantity() >= amount:
                product.decrease_quantity(amount)
                self.__money += product.get_price() * amount
                if product.get_quantity() == 0:
                    print(f"The item: {product.get_name()} is sold out")
            else:
                print(f"This quantity ({amount}) cannot be sold as there are only ({product.get_quantity()}) {product.get_name()}(s) remaining in stock.")
        else:
            print("Product not found.")

    # Find a product by its ID
    def find_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    # Markup prices for all products
    def markup_prices(self, multiplier):
        if multiplier > 0:
            for product in self.__products:
                new_price = round(product.get_price() * multiplier, 2)
                product.set_price(new_price)

    # String representation of the store
    def __str__(self):
        store_info = (f"Store Name: {self.__name}\n"
                      f"Current Holdings: ${self.__money:.2f}\n"
                      f"Current Stock:\n")
        if not self.__products:
            store_info += "No products available."
        else:
            for product in self.__products:
                store_info += f"===========\n{product}===========\n"
        return store_info

# Testing the Store class
store = Store("SLEEP TOKEN", 1000.0)
store.order_product(product1, 2)
store.order_product(product2, 4)
store.sell_product(1, 2)
store.markup_prices(1.1)

print(store)
