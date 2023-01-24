# wap to find out that any social media post is talking about Gaurang.
a=input("Enter the post: ")



a=a.lower()
a=a.find("gaurang")
if(a>=0):
    a=str(a)
    print("True"  + "Found in Post.")
    print(a +   "index at which Gaurang is written.")
    
else:
    print("false" +  "Not iN that Post.")