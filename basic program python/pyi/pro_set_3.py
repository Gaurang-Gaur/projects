# can we have a set with 18 and "18"
s={"18",18,3}
print(s)
print(len(s))
# What will be the length of set
# s.add(20)
#s.add(20.0)
#s.add("20")

print("\n \n ")
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)
# what is the type of s?
s={}
print(type(s))