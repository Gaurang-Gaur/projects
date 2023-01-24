# b="Gaurang"
# print(b)
# print(type(b))
# cc='I am Good boy:"s'
# print(cc)
# d='''"I really want's to learn to code to solve bigger picture."'''
# print(d)
# day="Thrusday"
# date="21/07/2022"
# #or c=day+date
# #print(c)
# print(day+date)#cancatenation
                         #string slicing....
# name="Gaurang"
# print(name[0])
# #name[3]="d"-->< you cann't modify the string in the system...

# print(name[3])
# print(name)
# name="A Good day."
# print(name[0:3]) # here the index zero in include in string slicing but we cann't include 3
# print(name[2:4])
# print(name[:5])#5 will be exclude from the string slicing and it should not be there
# Negative indicies...
#Why to use negative indicies when we have positive index already in string slicing...
# print(name[1:])
# print(name[0:])#if we leave last place of the string then it will print the whole string... 
name="Harry"
# print(name[-4:-1])# Here also we didn't include the second place of square block here -1 and 
# # include the -4 in the string slicing 
# # Important to remember that while using negative index that it start with -1 and we use when we doesn't know  the 
# # length of string and want to print elements of last ...
# # name[-4:-1 ]== name[1:4]
# # let check that name[-3:-1]==name[1:3]
# c=name[-3:-1]
# print(c)
# c=name[1:3]
# print😂🤣
#                                    slicing with skiping value...
# d=name[1:4:1]# It's means that print name[1:4] ( Remember postive index start with zero not with one ...)
# print(d)#with skip value of one ...It mean one after one...
# d=name[1:4:2]#Overwriting...
# print(d)
                     # String function
# Game="life is the best game ever created according to me"
# print(Game)
# # using len() function to find the length of line...
# print(len(Game))
# # New function string.endswith()
# print(Game.endswith("created"))
# # function story.count() to find the occurence of word or letter.
# print(Game.count("a"))
# print(Game.count("me"))

# # function to capatilization of word in strings...
# print(Game.capitalize())# It' s just capitalize the first word of string only...
                    # Escape squence character
# Escape squence character comprise of more than one character but represent of one character when use
# within the string

# write a python program to display a user content name followed by Good afternoon
#using input() function.
# name=input("Enter the name:\n ");
# print("Good afternoon, "+name)# contenation 

