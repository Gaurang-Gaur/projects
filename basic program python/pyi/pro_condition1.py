# Greatest of four Number...
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=int(input("Enter the value of d: "))
print(a)
print(b)
print(c)
print(d)
if(a>b and b>c and c>d):
    print("a is the greatest:")
elif(b>a and b>c and c>d):
    print("b is greatest:")
elif(c>a and c>b and c>d):
    print("c is the greatest")
else:
    print("d is the greatest")
    