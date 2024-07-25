class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Create an instance of the Dog class
my_dog = Dog("Buddy", 5)

# Access the attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
print(my_dog.bark())  # Output: Buddy says woof!



#JS


# class Dog {
#      Constructor to initialize the object
#     constructor(name, age) {
#         this.name = name;
#         this.age = age;
#     }

#      Method to define behavior
#     bark() {
#         return `${this.name} says woof!`;
#     }
# }

#  Create an instance of the Dog class
# const myDog = new Dog('Buddy', 5);

#  Access the properties and methods
# console.log(myDog.name);  // Output: Buddy
# console.log(myDog.age);   // Output: 5
# console.log(myDog.bark());  // Output: Buddy says woof!
