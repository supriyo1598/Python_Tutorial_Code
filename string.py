s=input("Enter any string:")
k=s.lower()
count=0
for i in k:
    if(i=='o' or i=='a' or i=='i' or i=='e' or i=='u'):
        count+=1
print("number of o:",count)
