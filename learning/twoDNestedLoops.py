twoD = [
    #0 1 2  
    [1,2,3],#0 
    [4,5,6],#1 
    [7,8,9] #2 
]

# print(twoD[1][1]) # prints 5
for i in twoD:
    print(i) # print each row/index in towD  
    for j in i: 
        print(j) # print each row/index in i  

# [1, 2, 3]
# 1
# 2
# 3
# [4, 5, 6]
# 4
# 5
# 6
# [7, 8, 9]
# 7
# 8
# 9