def myfunc(n):
    return lambda a: a*n

myd=myfunc(2)
print(myd(11))    
