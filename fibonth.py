nterms=int(input("upto which term?"))
n1=0
n2=1
if nterms<0:
    print("Please enter +ve integer")
elif nterms==0:
    print("Fibonacci series upto ",nterms,":")
    print(n1)
else:
    print("Fibonacci Series:")
    while n1<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
