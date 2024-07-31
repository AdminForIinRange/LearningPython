# Define the Snake class
class Snake:
    """
    Represents a real-world snake with basic behaviors.
    """

    def __init__(self, name, nickname, cry):
        """
        Initializes the Snake object with a name, nickname, and cry sound.
        """
        self.name = name
        self.nickname = nickname
        self.cry = cry

    def speak(self):
        """
        Outputs the cry sound of the snake.
        """
        print(self.cry)

    def coil(self):
        """
        Outputs a message indicating that the snake coils up its body.
        """
        print(f"{self.name} coils up its own body.")


# Define the Cat class
class Cat:
    """
    Represents a real-world cat with basic behaviors.
    """

    def __init__(self, name, nickname, cry):
        """
        Initializes the Cat object with a name, nickname, and cry sound.
        """
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.explored_locations = []  # List to track locations the cat has explored

    def speak(self):
        """
        Outputs the cry sound of the cat.
        """
        print(self.cry)

    def explore(self, location):
        """
        Adds a location to the explored locations list and outputs a message.

        Args:
            location (str): The location the cat is exploring.
        """
        self.explored_locations.append(location)
        print(f"{self.name} is exploring {location}.")


# Define the Sheep class
class Sheep:
    """
    Represents a real-world sheep with basic behaviors.
    """

    def __init__(self, name, nickname, cry, current_hunger):
        """
        Initializes the Sheep object with a name, nickname, cry sound, and hunger level.
        """
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.min_hunger = 0  # Minimum hunger level (not hungry)
        self.max_hunger = 100  # Maximum hunger level (extremely hungry)
        self.current_hunger = current_hunger  # Current hunger level

    def speak(self):
        """
        Outputs the cry sound of the sheep.
        """
        print(self.cry)

    def eat(self, food_sustenance):
        """
        Allows the sheep to eat and reduce its hunger level.

        Args:
            food_sustenance (int): The amount of sustenance provided by the food.

        Outputs:
            A message depending on whether the food is acceptable and the updated hunger level.
        """
        if food_sustenance <= 0:
            print("I cannot eat this non-nutritious meal.")
        elif food_sustenance > self.current_hunger:
            print("That is too much food to consume.")
        else:
            self.current_hunger -= food_sustenance
            print(f"Hunger reduced. Current hunger: {self.current_hunger}")


# Define the Mouse class
class Mouse:
    """
    Represents a real-world mouse with basic behaviors.
    """

    def __init__(self, name, nickname, cry):
        """
        Initializes the Mouse object with a name, nickname, and cry sound.
        """
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.has_cheese = False  # Boolean to track if the mouse has cheese

    def speak(self):
        """
        Outputs the cry sound of the mouse.
        """
        print(self.cry)

    def collect_cheese(self):
        """
        Allows the mouse to collect cheese.
        """
        self.has_cheese = True
        print(f"{self.name} has collected cheese.")

    def deposit_cheese(self):
        """
        Allows the mouse to deposit cheese.
        """
        self.has_cheese = False
        print(f"{self.name} has deposited cheese.")


# Define the Cow class
class Cow:
    """
    Represents a real-world cow with basic behaviors.
    """

    def __init__(self, name, nickname, cry):
        """
        Initializes the Cow object with a name, nickname, cry sound, and milk amount.
        """
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.milk_amount = 0  # Initial milk amount

    def speak(self):
        """
        Outputs the cry sound of the cow.
        """
        print(self.cry)

    def produce_milk(self):
        """
        Increases the cow's milk amount by 10 and checks if milking is required.
        """
        self.milk_amount += 10
        print(f"{self.name} has produced milk. Current milk amount: {self.milk_amount}")
        if self.milk_amount >= 30:
            self.milk()

    def milk(self):
        """
        Resets the cow's milk amount to 0 after milking.
        """
        print(f"{self.name} has been milked.")
        self.milk_amount = 0


# Example usage of the animal classes
if __name__ == "__main__":
    """
    Example code demonstrating the use of the animal classes.
    This block only runs when the script is executed directly, not when imported as a module.
    """

    # Create and test a Snake
    snake = Snake("Python", "Slither", "Hiss")
    snake.speak()
    snake.coil()

    # Create and test a Cat
    cat = Cat("Whiskers", "Kitty", "Meow")
    cat.speak()
    cat.explore("the garden")

    # Create and test a Sheep
    sheep = Sheep("Dolly", "Woolly", "Baa", 50)
    sheep.speak()
    sheep.eat(20)
    sheep.eat(70)

    # Create and test a Mouse
    mouse = Mouse("Jerry", "Little", "Squeak")
    mouse.speak()
    mouse.collect_cheese()
    mouse.deposit_cheese()

    # Create and test a Cow
    cow = Cow("Bessie", "Moo", "Moo")
    cow.speak()
    cow.produce_milk()
    cow.produce_milk()
    cow.produce_milk()
