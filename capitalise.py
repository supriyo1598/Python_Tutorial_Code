str=input("Enter your line:")
lower=0
upper=0
space=0
number=0
for i in range(0,len(str)):
    if str[i].isspace():
        space+=1
    elif str[i].islower():
        lower+=1
    elif str[i].isnumeric():
        number+=1
    else:
        upper+=1

print("Number of space:",space)
print("Number of lower:",lower)
print("Number of upper:",upper)
print("Number of numeric values:",number)
