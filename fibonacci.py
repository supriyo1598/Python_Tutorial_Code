nterms=int(input("How many terms?"))
n1=0
n2=1
count=0
if nterms<=0:
    print("Please enter +ve integer")
elif nterms==1:
    print("Fibonacci series upto ",nterms,":")
    print(n1)
else:
    print("Fibonacci Series:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
