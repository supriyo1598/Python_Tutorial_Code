def compound(time,rate,principle):
    p=1.0+(rate/100)
    x=p**time
    c=principle*x
    ci=c-principle
    print("Compound Interest:",ci)

t=float(input("Enter the time:"))
r=float(input("Enter the rate:"))
p=float(input("Enter the principle:"))
compound(t,r,p)
