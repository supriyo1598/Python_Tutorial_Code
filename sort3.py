a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
max=0
min=0
mid=0
if a>=b:
    if a>=c:
        max=a
    else:
        max=c
else:
    if b>c:
        max=b
    else:
        max=c
if a<b:
    if a<c:
        min=a
    else:
        min=c
else:
    if b<c:
        min=b
    else:
        min=c

if a==max and b==min:
    mid=c
elif a==min and b==max:
        mid=c
elif a==max and c==min:
    mid=b
elif a==min and c==max:
        mid=b
elif b==max and c==min:
    mid=a
elif b==min and c==max:
        mid=a
print(min," ",mid," ",max)
