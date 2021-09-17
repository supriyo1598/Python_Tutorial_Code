thislist=["apple","banana","lemon","cherry","mango"]  #create List
print(thislist)                            #print list
print(thislist[-1])                         #print a index
print(thislist[-2])                        #negative index
print(thislist[2:5])                       #range index
thislist[1]="melon"                        #change
print(thislist)
thislist.sort()                            #sort
print(thislist)
thislist.sort(reverse=True)                #rev sort
print(thislist)
thislist.append("Orange")                  #insert last
print(thislist)
thislist.insert(2,"banana")                #insert any position
print(thislist)
thislist.remove("apple")                   #remove element
print(thislist)
thislist.pop()                             #remove last element
print(thislist)
del thislist[2]                            #remove one index
print(thislist)
mylist=thislist.copy()                     #copy
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2                                   #join
print(l3)
thislist.append("Orange")                  #insert last
print(thislist)
thislist.append("Orange")                  #insert last
print(thislist)
thislist=list(dict.fromkeys(thislist))
print(thislist)
