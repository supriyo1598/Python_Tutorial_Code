def facto(n):
    fact=1
    if(n==0):
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact=fact*i
        print("The Factorial of",n,"is",fact)

num=int(input("Enter the number:"))
facto(num)
facto(7)
