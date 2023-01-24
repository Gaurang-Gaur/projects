# A spam comment is defined as a text containing following keyboard:
#"Make a lot money ","buy now", "subscribe this","Click this ".Wap ro detect the spams.



from importlib.abc import TraversableResources
from tkinter.tix import Tree


comment=input("\n Enter the text:")
spam=False
if("make a lot money" in comment):
    spam=True
    print("Attention Spam")
elif("buy now" in comment):
    spam=True
    print("Attention Spam")
elif("click this" in comment):
    spam=True
    print("Attention Spam")
elif("subscribe this" in comment):
    spam=True
    print("Attention spam")
else:
    print("Not a Spam ...")

if(spam==True):
    print("May be reported spam ahead")
else:
    print("Not a |Spam|")