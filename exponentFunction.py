def raise_to_power(base_num, pow_num):
    res = 1
    for i in range(pow_num):
        res = res * base_num
    return(res)
      

print(raise_to_power(5,2))
