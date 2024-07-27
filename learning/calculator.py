num1 = float(input("Enter a number: "))
op = str(input("operation: "))
num2 = float(input("Enter another number: "))

if (op == "+"):
    print(num1 + num2)
elif (op == "-"):
    print(num1 - num2) 
elif (op == "%"):
    print(num1 % num2)
elif (op == "x"):
    print(num1 * num2)
else:
    print(" Sorry, invalid operation, only: + - % x")



