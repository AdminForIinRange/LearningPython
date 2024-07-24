def translate(phrase):
    translation = ""
    for i in phrase:
        print(i) # print for each individual letters (i) in phrase 
        if i in "AEIOUaeiou": # if  each individual letters (i) in phrase has AEIOUaeiou
            print(translation)
            translation += "g" # translation = translation +"g" each each individual letters (i)
        else:
            translation += i
    return translation




print(translate("hello"))