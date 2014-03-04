arr=[1,1,2,3,3,4,4]
sum=0
for i in range (0,len(arr)):
    sum=sum^arr[i]
print(str(sum))