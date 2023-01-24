#wap to input eight no. from the user and display all the unique no.(once)
# when you see the unique in python in means {|set|}.
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
num3=int(input("Enter the number 3:"))
num4=int(input("Enter the number 4:"))
num5=int(input("Enter the number 5:"))
num6=int(input("Enter the number 6:"))
num7=int(input("Enter the number 7:"))
num8=int(input("Enter the number 8:"))
s={num1,num2,num3,num4,num5,num6,num7,num8}
print(list(s))
d=s.sort()
print(d)