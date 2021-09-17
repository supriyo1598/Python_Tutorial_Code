thisdict={
"brand":"Tata",
"model":"Swift",
"year":2010
}
x=thisdict.get("model")
print(x)

thisdict["year"]=2015

for x,y in thisdict.items():
    print(x, y)

if "model" in thisdict:
    print("Yes present")

print(len(thisdict))

thisdict["colour"]="black"
print(thisdict)

del thisdict["model"]
print(thisdict)
