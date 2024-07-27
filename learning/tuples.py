# tuples are unchangeable and not like array's/List's
# tuples are immutable, meaning they cannot be changed
# tuples are often used when you want to group multiple values together
# but you don't want those values to be changed
# one special case where tuples are used is when you use a tuple as a key in a dictionary
# because dictionaries use the hash value of the key to keep track of the items
# and tuples have a fixed hash value so they can be used as keys

cord = (4,6) # 4 is x and 6 is y and 4 is 0 and 6 is 1

# cord[0] = 10 # this will throw an error

print(cord[0]) # prints 4

cordArr = [(4,6), (7,8), (9,10)] # this is a list of tuples, tuples are immutable so the tuples cannot be changed but the list can be changed
cordArr[1] = (1,2) # changes the second tuple to (1,2)

print(cordArr)