# Creating my own dictionary...
dict={
    "phool":"Flower",
    "pade":"tree",
    "pani":"Water"
}
print( "Your option are:",dict.keys())

a=input("Enter the word for meaning:")

print("Meaning of your word:",dict[a])# it's more better to use the get( ) because 
# it will not throw error hence avoiding avoidable crashes in system...
print(dict.get(a))