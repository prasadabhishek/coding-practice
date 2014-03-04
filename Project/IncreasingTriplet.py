arr=[1,2,3,4,5,6,7,8,9]


for i in range(0,len(arr)):
    if((i-1)>=0 and (i+1)<len(arr)):
        if(arr[i]>arr[i-1] and arr[i]<arr[i+1]):
            for j in range(i-1,i+2):
                print(str(arr[j]),end='')
            print("")