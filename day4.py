'''a=["apple", "banana","grapes"]
print(a)

a=["apple", "banana","apple"]
print(a)

a=["apple", "banana","grapes"]
print(len(a))

a=["dk","dj","dynamo"]
b=[2,6,7,18]
c=[11.5,5.8,8.9]
print(a)
print(b)
print(c)

x=["hi",7,"hello",1,51,23,4.5,7.8]
print(x)

x=["hi",7,"hello",1,51,23,4.5,7.8]
print(type(x))

fruits=list(("apple","orange","grapes"))
print(fruits)

x=["apple", "orange","watermelon","grapes"]
print(x[1])
print(x[-1])
print(x[-2])
print(x[1:3])
print(x[1:])
print(x[:1])
if "grapes"in x:
    print("it is present in the list")

a=["black current","choclate","vanilla","belgium","butterscotch"]
a[2]="roasted almond"
print(a)
a[1:4]="red velvet","chikku almond","kesar pista"
print(a)

a=["black current","choclate","vanilla","belgium","butterscotch"]
a.append("choclate")
print(a)

a=["black current","choclate","vanilla","belgium","butterscotch"]
a.insert(1,"arabian delight")
a.insert(4,"hawain punch")
print(a)

a=["choclate","vanilla"]
b=["butterscotch","oreo"]
print(a+b)
a.extend(b)
print(a)

a=["choclate","vanilla"]
b=("butterscotch","oreo")
a.extend(b)
print(a)

x=["black current","choclate","vanilla","belgium","butterscotch"]
x.remove("vanilla")
print(x)

x=["black current","choclate","vanilla","belgium","butterscotch"]
x.pop(2)
print(x)

bike=["ninja","ducati","xpulse210","himalayan"]
bike.clear()
print(bike)
#tasks
a=["udupi","manglore","darmasthala","hassan"]
a[2]="hubli"
print(a)

x=["lost in space","squid game","kota factory"]
x.insert(0,"go go squid")
print(x)

x=["lost in space","squid game","kota factory","go ahead"]
x.insert(2,"go go squid")
print(x)

cricket=["ICT","RCB","KB","CSK"]
cricket.remove("CSK")
print(cricket)

a=[48,15,96,47,78,23,]
a.sort()
print(a)

x=["a","c","x","g","r","z"]
x.sort()
print(x)

a=["anna","dynamo","dk","dj"]
a.append("srishti")
print(a)
a.sort()
print(a)

x=["coding","sleeping","reading","music"]
x.pop(0)
x.append("python")
print(x)
'''
x=["coding","sleeping","reading","music"]
x.pop(0)
x.insert(0,"python")
print(x)
