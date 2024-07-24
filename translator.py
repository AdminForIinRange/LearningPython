def translate(phrase):
    translation = ""
    for i in phrase:
        print(i) # print for each individual letters of phrase (i) in phrase 
        if i in "AEIOUaeiou": # if  each individual letters of phrase (i) in phrase has AEIOUaeiou
            print(translation)
            translation += "g" # translation = translation +"g" each each individual letters of phrase (i)
        else:
            translation += i # translation = translation (empty or what ever translation is at) + each each individual letter of phrase (i) , 
    return translation # returns: hgllg


print(translate("hello")) # prints: hgllg


# basically if from Hello, teh for loop will index through the word "hello" so
# 
# i =
#    
# h: 0 
# e: 1
# l: 2
# l: 3
# o: 4

# h (i = 0 ) dose not have "AEIOUaeiou" so it runes the 

# else:
# translation += i  

#So translate at this stage is: translation = "h" NEXT ITERATION OF PHRASE


# i =
#    
# h: 0 ( translation = "h" )
# e: 1
# l: 2
# l: 3
# o: 4

# e (i = 1 ) dose have "AEIOUaeiou" so it runs:
# 
# if i in "AEIOUaeiou":
# translation += "g"

#So translate at this stage (i = 1) is: translation = "hg" NEXT ITERATION OF PHRASE


# i =
#    
# h: 0 ( translation = "h" )
# e: 1 ( translation = "hg" )
# l: 2
# l: 3
# o: 4