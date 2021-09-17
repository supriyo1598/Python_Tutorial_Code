def selectionsort(nlist):
    i=0
    n=len(nlist)
    while i<n-1:
        min_index=i
        j=i+1
        while j<n:
            if nlist[j]<nlist[min_index]:
                min_index=j
            j=j+1
        x=nlist[i]
        nlist[i]=nlist[min_index]
        nlist[min_index]=x
        i=i+1

nlist=[14,12,16,17,15]
selectionsort(nlist)
print(nlist)                
