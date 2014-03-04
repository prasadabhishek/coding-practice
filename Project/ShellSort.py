#shell search
arr=[2,50,11,71,71,65,45,13,98,6]
gap=len(arr)
noComp=0;

while(gap!=1):
    gap=int(gap/2)
    for i in range(gap,len(arr)):
        t=i
        k=i-gap
        while(k>=0):
            noComp+=1
            if(arr[i]<arr[i-gap]):
                temp=arr[i]
                arr[i]=arr[i-gap]
                arr[i-gap]=temp
                i=i-gap
                k=i-gap
            else:
                break
        i=t
            

print(arr)

print("\n No. of Comparisons : " + str(noComp))