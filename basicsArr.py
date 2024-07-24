arr = ["andrew", "bob", "charlie", "donald"]

numsArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr.extend(numsArr) # appends all the elements of numsArr to the end of the array
 
arr.append(11) # appends 11 to the end of the array

arr.insert(0, "hello") # inserts the element at the specified index

arr.remove("bob") # removes the first element with the value "bob"

arr.pop() # removes the last element or the element at the specified index like pop(0) or pop(-1) will remove the element

# arr.clear() # removes all elements from the array

arr.index("bob") # returns the index of the first element with the value "bob"

arr.sort() # sorts the array in ascending order

arr.reverse() # reverses the array

arr.count("bob") # returns the number of elements with the value "bob"

arr.copy() # returns a copy of the array


print(arr)
