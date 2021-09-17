a=int(input("Enter the number:"))
n=a
sum=0
while a!=0:
    r=a%10
    x=r**3
    sum=sum+x
    a=a//10
if sum==n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
