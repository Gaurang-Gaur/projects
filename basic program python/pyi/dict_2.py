# Creating my own dictionary...
dict={
"day":"Sunday",
"Date":"24/07/22",# You have to make key and value of same data type otherwise it will throw error
"work":"Reaching the game in python",
"anotherdict":{"God":"Help us all"},
 1:3 
}
print(dict["anotherdict"]["God"])
print(list(dict.keys()))
print(list(dict.values()))
print(dict.items())
uptdict={
    "Friend":"loner",
    "bannana":"A fruits",
    "Date":"2/03/22"# key  are mutable we can't make to same name key in dictionary otherwise it will 
    # overwrite in it.
}
dict.update(uptdict)# To update teh dictionary by adding key value pair from updatedict...
print( "\n \n \n ")
print(dict)
# IMPORTANT what is difference between below two?

print(dict["day"])
print(dict.get("day"))
print(dict.get("to"))# It willnot throw a error in fact it will show none ...
print(dict["to"])# It will throw error because it is your responsible to have such a key in dictionary while using 
# such type of call in dictionary...
