#wap to print yes when the age entered by the user is greater than or equal to 18.
a=input("Enter the age:")
print(a)
a=int(a)# if this code is miss than it will throw an error because input take input as string 
# but for comparsion in if condition we need the integer no...

if(a>=18):
    print("The age is greater than or equal to 18:")
else:
    print("Not true:")