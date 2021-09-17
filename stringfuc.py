str="This is the class of computer science We are learning python for computer ."
list=str.rsplit(" ")
print(list)
count=0
for i in range(0,len(list)):
    if list[i]=="computer":
        count+=1
print("number of words:",count)        
