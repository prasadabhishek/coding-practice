A=[4,2,5,2,7,5,9,12,54,121,2]
lngth=len(A)

def heapify(A,length):
    count=0
    for i in range(0,length):
        if(2*i+1 < length):
            if(A[i]<A[2*i+1]):
                temp=A[i]
                A[i]=A[2*i+1]
                A[2*i+1]=temp
                count+=1
        if(2*i+2 < length):
            if(A[i]<A[2*i+2]):
                temp=A[i]
                A[i]=A[2*i+2]
                A[2*i+2]=temp
                count+=1
    return count

def doheapify(A,length):
    i=-121
    while(i!=0):
        i=heapify(A,length)


def sort(A,length):
    for i in range(length-1,1,-1):
        temp=A[0]
        A[0]=A[i]
        A[i]=temp
        length=length-1
        doheapify(A,length)

def heapsort(A):
    doheapify(A,len(A))
    sort(A,len(A))


heapsort(A)
print("done")