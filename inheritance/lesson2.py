# Superclass
class Material:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display_info(self):
        print(f"Material: {self.name}, Quantity: {self.quantity}")

    def add_quantity(self, amount):
        self.quantity += amount
        print(f"Added {amount} to {self.name}. New quantity: {self.quantity}")

    def use_quantity(self, amount):
        if amount > self.quantity:
            print(f"Not enough {self.name} in stock!")
        else:
            self.quantity -= amount
            print(f"Used {amount} of {self.name}. Remaining quantity: {self.quantity}")

# Subclass
class PerishableMaterial(Material):
    def __init__(self, name, quantity, expiration_date):
        super().__init__(name, quantity)
        self.expiration_date = expiration_date

    def display_info(self):
        super().display_info()
        print(f"Expiration Date: {self.expiration_date}")

    def check_expiration(self, current_date):
        if current_date > self.expiration_date:
            print(f"{self.name} has expired!")
        else:
            print(f"{self.name} is still good until {self.expiration_date}")

# Main function
def main():
    # Create a general material object
    steel = Material(name="Steel", quantity=100)
    steel.display_info()
    steel.add_quantity(50)
    steel.use_quantity(30)

    print("\n")  # For better readability

    # Create a perishable material object
    milk = PerishableMaterial(name="Milk", quantity=20, expiration_date="2024-07-01")
    milk.display_info()
    milk.add_quantity(10)
    milk.use_quantity(5)
    milk.check_expiration(current_date="2024-06-10")

if __name__ == "__main__":
    main()
