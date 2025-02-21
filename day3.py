a=int(input("father's age:"))
b=int(input("son's age:"))
print("addition:", a+b)
print("subtraction:", a-b)
print("multiplication:",a*b)
print("division:", a/b)
print("modulus:", a%b)
print("floor:",a//b)
print("exponential:",a**b)

a=int(input("enter the price of item 1:"))
b=int(input("enter the price of item 2:"))
print("reminder:",a%b)

a=int(input("length of the rectangle:"))
b=int(input("breadth of rectangle:"))
print("area of rectangle :", a*b)

a=8
b=8
print(a==b)
if(a==b):
    print("a is equal to b")

x=8
y=10
if(x!=y):
    x+=y
    print(x)

x=18
y=10
if(x!=y):
    x-=y
    print(x)

x=18
y=2
if(x!=y):
    x*=y
    print(x)

a=int(input("enter the age:"))
if(a>=18):
    print("eligible for driving car")
else:
    print("not eligible for driving the car")

x=int(input("enter a number:"))
if(x%2==0):
    print("number is even")
else:
    print("number is odd")

a=int(input("enter the marks of student:"))
if(a>=80):
    print("pass")
elif(a>=75 and a<80):
    print("fail but eligible for re-exam")
else:
    print("fail")

x=int(input("enter the marks"))
if(c>=90):
    print("Grade A")
elif(c>=80 and c<90):
    print("Grade B")
elif(c>=70 and c<80):
    print("Grade C")
elif(c>=60 and c<70):
    print("Grade D")
elif(c>=50 and c<60):
    print("Grade E")
else:
    print("Grade F")

a=int(input("enter the obtained marks:"))
b=int(input("enter the total marks:"))
c=(a/b)*100
print("percantage is:",c)
if(c>=90):
    print("Grade A")
elif(c>=80 and c<90):
    print("Grade B")
elif(c>=70 and c<80):
    print("Grade C")
elif(c>=60 and c<70):
    print("Grade D")
elif(c>=50 and c<60):
    print("Grade E")
else:
    print("Grade F")

a=int(input("enter the mark of subject 1:"))
b=int(input("enter the mark of subject 2:"))
c=int(input("enter the mark of subject 3:"))
if(a>=80 and b>=80 and c>=80):
    print("u have passed")
else:
    print("u have failed one or more subjects")

a=int(input("sales of A:"))
b=int(input("sales of B:"))
c=int(input("sales of C:"))
if(a>=b and a>=c):
    print("company A has higher sales")
elif(b>=a and b>=c):
    print("company B has higher sales")
else:
    print("company C has higher sales")

#assignment
a=int(input("enter the sales of the employee:"))
if(a>=60000):
    print("u are eligible to run the organization")
else:
    print("u are not eligible to run the organization")


