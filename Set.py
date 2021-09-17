thisSet={"apple","banana","lemon","cherry","mango"}  #create Set
print(thisSet)                            #print Tuple

print("banana" in thisSet)

thisSet.add("melon")
print(thisSet)

thisSet.update(["Orange","grapes"])
print(thisSet)

print(len(thisSet))

thisSet.remove("melon")
print(thisSet)

l1={1,2,3}
l2={3,4,5,6}
l3=l1.union(l2)                                   #join
print(l3)
