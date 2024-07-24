# Conditional Statements and more boolean values
tall = True
male = False

print(tall and male) # prints False because both are false
print(tall or male) # prints True  because at least one is true 
print(not tall) # prints False because tall is true


if tall and male:
    print("you are tall and male, both are true")
elif tall or male:
    print("you are tall or male, one or both are true")
else:
    print("you are not tall or not male, one or both are false")