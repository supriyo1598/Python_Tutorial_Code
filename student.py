class student:                                   #Parent Class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        print(self.fname+" "+self.lname)

class topper(student):                         #Child Class
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.hmarks=850

x=topper("Supriyo","Sarkar")
x.display()
print(x.hmarks)
