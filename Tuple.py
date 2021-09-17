thisTuple=("apple","banana","lemon","cherry","mango")  #create Tuple
print(thisTuple)                            #print Tuple
print(thisTuple[1])                         #print a index
print(thisTuple[-2])                        #negative index
print(thisTuple[2:5])                       #range index

y=list(thisTuple)
y[2]="orange"                                  #update tuple
thisTuple=tuple(y)

print(thisTuple)

if "orange" in thisTuple:                      #present check
    print("yes present")

print(len(thisTuple))                          #tuple Length

l1=(1,2,3)
l2=(4,5,6)
l3=l1+l2                                   #join
print(l3)
