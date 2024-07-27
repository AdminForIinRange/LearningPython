# example of try catch
try:
    print(1/0) 
except ZeroDivisionError:
    print("You cant divide by zero")

try:
    print(int("hello"))
except ValueError:
    print("You cant convert a string to an int")

try:
    print(a)
except NameError:
    print("You cant print a variable that doesnt exist")
