arr=[1,2,3,4,2,2,2]
k=6

def twosum(arr,i,k):
    i=i
    j=len(arr)-1
    list=[]
    while (i<j):
        if(arr[i]+arr[j]>k):
            j-=1
        elif(arr[i]+arr[j]<k):
            i+=1
        else:
            list.append(arr[i])
            list.append(arr[j])
            return list
    return list

def threesum(arr,k):
    list=[]
    res=[]
    arr.sort()
    for i in range(0,len(arr)):
        sum=0
        list=twosum(arr,i+1,k-arr[i])
        for j in range(0,len(list)):
            sum+=list[j]
        if(arr[i]+sum == k):
           list.append(arr[i])
           list.sort()
           if(list not in res):
            res.append(list)
    return res

list = threesum(arr,k)
if(len(list)==0):
    print("no such pair")
else:
    print(list)

