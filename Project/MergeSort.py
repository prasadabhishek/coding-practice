import math
a=[38,27,43,3,9,82,10]

def mergesort(a,start,end):
    if(start==end):
        return
    mid=int(math.floor((start+end-1)/2))
    if(end-start>2):
        mergesort(a,start,mid+1)
        mergesort(a,mid+1,end)
    i=start
    while(i<=mid and mid+1!=end):
        j=mid+1
        while(j<end):
            if(j<len(a) and i<len(a)):
                if(a[i]>a[j]):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
                    i+=1
                else:
                    if(j<len(a)-1 and i<len(a)-1):
                        j+=1
                    break
                if(end-start<=2):
                    break
                    #i+=1
            else:
                i+=1
                break
mergesort(a,0,len(a))
