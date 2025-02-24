#tasks
#sum of 2 numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(a+b)

#sum of 3 numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
print(a+b+c)

#check odd or even
x=int(input("enter the number:"))
if (x%2)==0:
    print("even")
else:
    print("odd")

#factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
a=int(input("enter a number: "))
print("factorial:",factorial(a))

#largest in three numbers
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
z=int(input("enter the third number: "))
if x>y and x>z:
    print("largest number is: ",x)
elif y>x and y>z:
    print("largest number is: ",y)
else:
    print("largest number is: ",z)

#check for palindrome
a=input("Enter an input: ")

if a==a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#fibbonacci series
n=int(input("enter a number:"))
a,b=0,1
print("fibbonacci series:",end=" ")
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b

#count vowels:
a=input("enter a sentence: ").lower()
vowels="aeiou"
count=0
for char in a:
    if char in vowels:
        count+=1
print("Number of vowels:", count)

#count consonants:
a=input("enter a sentence: ").lower()
vowels="aeiou"
count=0
for char in a:
    if char not in vowels:
        count+=1
print("Number of consonants:", count)

#prime numbers
n=int(input("enter a number"))
if n>1:
    for i in range(2,(n//2)+1):
        if (n%i)==0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

#multiplication table
n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}×{i}={n*i}")

#TUPLES
a=("deeksha",)
print(type(a))

a=("deeksha",)
v=list(a)
print(type(v))

x=("hello","hi")
y=list(x)
y.append("how")
y[1]="hfdjj"
x=tuple(y)
print(x)

x=("hello","hi")
y=list(x)
y.remove("hi")
x=tuple(y)
print(x)

x=("hello","hi")
y=list(x)
y.insert(1,"wow")
x=tuple(y)
print(x)

ic=("chikku almond","vanilla")
ic2=("butterscoch","rosted almond")
a=list(ic)
b=list(ic2)
a.extend(b)
ic=tuple(a)
ic2=tuple(b)
print(ic)

x=("hello","hi")
y=list(x)
y.pop(1)
x=tuple(y)
print(x)


