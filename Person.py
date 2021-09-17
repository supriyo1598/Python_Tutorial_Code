class Person:
    def __init__(sarthok,name,age):
        sarthok.name=name
        sarthok.age=age

    def display(vinit):
        print("My name is:"+vinit.name)

p1=Person("John",54)
print(p1.name)
print(p1.age)
p1.age=40;
print(p1.age)
p1.display()
del p1.age
print(p1.age)
