def compute_hcf(x,y):
    if x>y:
        s=y
    else:
        s=x
    for i in range(1,s+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
     num1=int(input("Enter number 1: "))
 num2=int(input("Enter number 2: "))
    print("HCF is:",compute_hcf(num1,num2))
