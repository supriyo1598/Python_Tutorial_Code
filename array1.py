car=["Tata","BMW","Volvo"]      #Create array
x=car[2]
print(x)                        #print single element
length=len(car)                 #length of the array
print(length)
for a in car:                   #print full array
    print(a)
car.append("Honda")             #Adding a element
for a in car:
    print(a)
car.remove("BMW")               #remove element
for a in car:
    print(a)
car.sort()                      #sort element
for a in car:
    print(a)
