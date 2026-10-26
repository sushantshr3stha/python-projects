class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity =quantity

class Inventory(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.products = {}

    def add_products(self, name, price, quantity):
        if price<0 or quantity<0:
            return "Price or Quantity can't be negative"
        if name in self.products:
            self.products += quantity
            self.products[name].price = price
        else:
            self.products[name] = Product(name, price, quantity)
        print("product saved")


    def sell_product(self, name, quantity):
        product = self.products.get(name)

        if product is None:
            print("product not found")
        elif product <0:
            print("product cant be negative")
        elif quantity > product.quantity:
            print("not enough stock")
        else:
            product.quantity -= quantity
            print("sale completed")


    def show_inventory(self):
        for product in self.products.values():
            print(f"{product.name} \n Rs. {product.price:.2f} \n Stock: {product.quantity}")


    def total_value(self, product):
        return sum(
            product.price * product.quantity
            for product in self.products.values()
            )

inventory = Inventory()

inventory.add_products("Keyboard", 1200, 10)
inventory.add_products("Monitor", 12000, 10)

inventory.sell_product("Keyboard", 2)
inventory.show_inventory()

print(
    f"Total inventory value: "
    f"Rs. {inventory.total_value():.2f}"
)