class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def display(abc):
        print("Length:",abc.l)
        print("Breadth:",abc.b)

class area(rect):
    def __init__(self,l,b):
        rect.__init__(self,l,b)

    def findarea(abc):
        c=abc.l*abc.b
        print("Area:",c)

obj=area(8,4)
obj.display()
obj.findarea()
