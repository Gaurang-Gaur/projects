from math import factorial


num=int(input("Enter the value to find the factorial:"))
print("The no . you have entered:"+str(num))
print(type(num))

if(num==1):
    print("The value of factorial is 1:")
else:
    while(num!=1):
        fact=num*(num-1)
        num=num-1
print(factorial(5))