A=[51,0,0,0,3,33,19,59]

def quicksort(A,start,finish):
    if(start<finish):
        pivindex=partition(A,start,finish)
        quicksort(A,start,pivindex-1)
        quicksort(A,pivindex+1,finish)
    return

def partition(A,start,finish):
    pivot=A[start]
    forward=start+1
    backward=finish
    x=0
    y=0

    while(backward>forward):
        while(forward<finish):
            if(A[forward]>pivot):
                x=A[forward]
                break
            else:
                forward+=1
        while(backward>start):
            if(A[backward]<pivot):
                y=A[backward]
                break
            else:
                backward-=1
        if(backward>forward):
            A[forward]=y
            A[backward]=x
            forward+=1
            backward-=1


    A[start]=A[backward]
    A[backward]=pivot
    return backward

quicksort(A,0,len(A)-1)


print(A)