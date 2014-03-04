A=[-1,0,1,2,-1,4]

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

selectionsort(A)

main_list=[]
for i in range(0,len(A)-1):
    l=i+1
    r=len(A)-1
    while(l<r):
        if(A[i]+A[l]+A[r] == 0):
            if((str(A[i])+" , "+str(A[l])+" , "+str(A[r])) not in main_list):
                main_list.append(str(A[i])+" , "+str(A[l])+" , "+str(A[r]))
        if(A[i]+A[l]+A[r] < 0):
            l+=1
        else:
            r-=1

for i in range(0,len(main_list)):
    print(str(main_list[i]))