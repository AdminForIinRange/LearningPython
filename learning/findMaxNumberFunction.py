#Find Max Number Function 

def max_num(num1, num2, num3):
    arr = [num1, num2, num3]


    arr.sort()
    print(arr)
    
    if (num1 >= num2 and num1 >= num3):
        print(num1)
    elif (num2 >= num1 and num2 >= num3):
        print(num2)
    else:
        print(num3)

max_num(1,6,3)