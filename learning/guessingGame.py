# pretty proud of this lol did it all by my self and out preformed the youtube vid

correct = 1
trys = 3

print(str(trys) + "Trys left")
guess = input(str("Guess the number:"))
while guess != correct:

    if (trys == 0):
        print("you ran out of guesses")
        break
    else:
        trys -= 1
        print(str(trys) + "Trys left")
        guess = input(str("Incorrect, Guess the number :"))
      


print("Nice you got it!")

