# Snake class
class Snake:
    def __init__(self, name, nickname, cry):
        self.name = name
        self.nickname = nickname
        self.cry = cry

    def speak(self):
        print(self.cry)

    def coil(self):
        print(f"{self.name} coils up its own body.")


# Cat class
class Cat:
    def __init__(self, name, nickname, cry):
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.explored_locations = []

    def speak(self):
        print(self.cry)

    def explore(self, location):
        self.explored_locations.append(location)
        print(f"{self.name} is exploring {location}.")


# Sheep class
class Sheep:
    def __init__(self, name, nickname, cry, current_hunger):
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.min_hunger = 0
        self.max_hunger = 100
        self.current_hunger = current_hunger

    def speak(self):
        print(self.cry)

    def eat(self, food_sustenance):
        if food_sustenance <= 0:
            print("I cannot eat this non-nutritious meal.")
        elif food_sustenance > self.current_hunger:
            print("That is too much food to consume.")
        else:
            self.current_hunger -= food_sustenance
            print(f"Hunger reduced. Current hunger: {self.current_hunger}")


# Mouse class
class Mouse:
    def __init__(self, name, nickname, cry):
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.has_cheese = False

    def speak(self):
        print(self.cry)

    def collect_cheese(self):
        self.has_cheese = True
        print(f"{self.name} has collected cheese.")

    def deposit_cheese(self):
        self.has_cheese = False
        print(f"{self.name} has deposited cheese.")


# Cow class
class Cow:
    def __init__(self, name, nickname, cry):
        self.name = name
        self.nickname = nickname
        self.cry = cry
        self.milk_amount = 0

    def speak(self):
        print(self.cry)

    def produce_milk(self):
        self.milk_amount += 10
        print(f"{self.name} has produced milk. Current milk amount: {self.milk_amount}")
        if self.milk_amount >= 30:
            self.milk()

    def milk(self):
        print(f"{self.name} has been milked.")
        self.milk_amount = 0


# Example usage
if __name__ == "__main__": # calling the func
    # Create and test Snake
    snake = Snake("Python", "Slither", "Hiss")
    snake.speak()
    snake.coil()

    # Create and test Cat
    cat = Cat("Whiskers", "Kitty", "Meow")
    cat.speak()
    cat.explore("the garden")

    # Create and test Sheep
    sheep = Sheep("Dolly", "Woolly", "Baa", 50)
    sheep.speak()
    sheep.eat(20)
    sheep.eat(70)

    # Create and test Mouse
    mouse = Mouse("Jerry", "Little", "Squeak")
    mouse.speak()
    mouse.collect_cheese()
    mouse.deposit_cheese()

    # Create and test Cow
    cow = Cow("Bessie", "Moo", "Moo")
    cow.speak()
    cow.produce_milk()
    cow.produce_milk()
    cow.produce_milk()
