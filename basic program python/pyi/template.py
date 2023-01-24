# Write program to fill in a letter template given below with name and date
#letter ="Dear <name>, 
# you are selected !
# <Date>"
#I am using triple quote for string and they are working fine.
letter='''Dear <name>, 

|you are selected !|

<Date>'''
name=input("Enter your Name:")
date=input("Enter your Date:")
letter=letter.replace("<name>",name) # using replace function in string program.
letter=letter.replace("<Date>",date)
print(letter)