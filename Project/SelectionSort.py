A=[3,4,1,2,7,1,34,22,12,2]

def selectionsort(A):
    low=0
    index=0
    for i in range(0,len(A)-1):
        swap=0
        low=A[i]
        for j in range(i+1,len(A)):
            if(low>A[j]):
                low=A[j]
                index=j
                swap=1
        if(swap==1):
            A[index]=A[i]
            A[i]=low
