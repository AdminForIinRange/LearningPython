class Student:
    def __init__(self, name, major, gpa, is_active):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_active = is_active

    def displayInfo(self):
        print(self.name, "\n", self.major, "\n", self.gpa)


# fix the code
student = Student("exmaple", "example", "example", "example")
student.displayInfo()
