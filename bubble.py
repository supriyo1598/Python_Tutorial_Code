def bubblesort(nlist):
    i=0
    n=len(nlist)
    while i<n-1:
        j=0
        sw=0
        while j<n-i-1:
            if nlist[j]<nlist[j+1]:
                x=nlist[j]
                nlist[j]=nlist[j+1]
                nlist[j+1]=x
                sw=1
            j=j+1
        if sw==0:
            break
        i=i+1

nlist=[14,12,10,13,15]
bubblesort(nlist)
print(nlist)
