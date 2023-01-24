#wap to find given  the prime no:

num=int (input("Enter  the no. to check: "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("This prime no:")
else:
    print("This no. not prime no.")
