p = int(input("Enter the marks of subject 1:"))
q  = int(input("Enter the marks of subject 2:"))
r = int(input("Enter the marks of subject 3:"))
s = int(input("Enter the marks of subject 4:"))
t = int(input("Enter the marks of subject 5:"))
m = p+q+r+s+t
print("Total marks :",m)
n = ((p+q+r+s+t)/500)*100#Mistake1.Not writing the correct formula as a logic (p+q+r+s+t)/500#
print("Percentage :",n)

if   (n >=90) :
    print( "Grade is A ", n  >  90)
elif  (n >= 80):
    print("Grade is B", n> 80)#Mistake 2 . We can use multiple elif in between if and else#
elif (n >= 70):
    print("Grade is C", n>70)
elif (n>=60):
    print("Grade is D", n> 70)
else :
    print(Fail)



