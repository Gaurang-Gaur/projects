#wap to greet all the person names stored in a list l1 and which start with S.
from re import S


l1=["harry","Sahil","Suraj","sunny","Rahul"]
for name in l1:# here name list item/object the created in for loop and then we use the dot to add the 
    if name.startswith("S" or "s"):
        print("hello "+ name)
