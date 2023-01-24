# Tuple are immutable as compared to list...
t=(34, 35 ,36 ,61,62,63,64,65,66,67,68,69,70,"Gaurang")
# c=t(0)
# print(c) tuple are not callable in program...
c=t.count(34)
print(c)
d=t.index(34)
print(d)
print(t)