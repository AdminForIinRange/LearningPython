class Student:
    def __init__(self, name, major, gpa, is_active):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_active = is_active

    def displayInfo(self):
        """
        Prints the student's name, major, and GPA.
        """
        print(self.name, "\n", self.major, "\n", self.gpa)


# fix the code
student1 = Student("exmaple", "example", "example", "example")
student1.displayInfo()  # displayInfo is a method of the student1 object
student1.displayInfo()




# class is a blueprint/template/schema
# object is an instance of a class, it is created by instantiating a class using the class name and the () operator
# each object has its own set of attributes and methods, and shares the same set of methods as other objects of the same class
# objects are created when we call the class name with the () operator
# objects are created to represent real-world objects or concepts, and they can have their own unique attributes and behaviors
# object is an instance of a class


