#Foor loop,think of for loops as map() like in JS

arr = ["mike", "steve", "donald"]
print("arr has " + str(len(arr)) + " items indexing from 1")

for i in range(len(arr)): #redundant because len() exits
    print(i)

# in JS this would be arr.map((index) =>{console.log(index)})

# But JS has its own For loops like:

# let arr = ["mike", "steve", "donald"];
# console.log("arr has " + arr.length + " items indexing from 1");

# for (let i = 0; i < arr.length; i++) {
#     console.log(i); 
# }