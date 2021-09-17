
def myfunc():
    x=300                      #Local Variable
    print(x)
    global y=100               #Global Variable
    def abc():
        print(x)                #Inner Function Variable
    abc()

myfunc()
