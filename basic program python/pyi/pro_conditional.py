#wap to find out whether a student is pass or fail , if it require total 40% and at least 30% in each subject 
# to pass . Assume 3 subject and take marks as an input from the user ...
m1=int(input("Enter the marks of subject 1:"))
m2=int(input("Enter the marks of subject 2:"))
m3=int(input("Enter the marks of subject 3:"))

avg=m1+m2+m3
tot=avg/3
if(tot>40 and m1>=30 and m2>=30 and m3>=30):
    print("Pass")
else:
    print("Fail")