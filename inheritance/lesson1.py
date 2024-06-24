# Superclass
class Animal:
    def make_sound(self):
        print("Animal sound")

# Subclass
class Dog(Animal):
    def make_sound(self):
        print("Woof")

# Main function
def main():
    my_animal = Animal()  # Create an Animal object
    my_dog = Dog()        # Create a Dog object

    my_animal.make_sound()  # Outputs: Animal sound
    my_dog.make_sound()     # Outputs: Woof

if __name__ == "__main__":
    main()
