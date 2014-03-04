#binary search
arr=[1,2,3,4,5,6,7,8,9,8]
start=0
end=len(arr)
length=end
x=int(input("Enter Element to Search : "))
mid=int(length/2)

while (length!=1):
       if(x==arr[0]):
           print("Found at position 0")
           break
       if(x==arr[mid]):
           print("Found at position :" + str(mid))
           break
       if(x<arr[mid]):
           length=int(length/2)
           end=mid 
           mid=int((start+end)/2)
       else:
           length=int(length/2)
           start=mid
           end=start+length
           mid=int((start+end)/2)