a=[3,4,5,1,2]


def findRot(a):
    start = 0
    end = len(a)
    mid = int((start+end)/2)

    if(a[start]>a[end-1]):
        while(start-mid!=-1):
            if(a[start]>a[mid]):
                end=mid
                mid = int((start+end)/2)
            else:
                start = mid
                mid = int((start+end)/2)
        return mid
    else:
        return 0

def findNum(a,x):
        start = 0
        end = len(a)-1
        mid = int((start+end)/2)
        while(start<end):
            if (a[mid]==x):
                return 1
            if(a[start]<=a[mid]):
                if(x<=a[mid] and x>=a[start]):
                    end=mid-1
                    mid = int((start+end)/2)
                else:
                    start=mid+1
                    mid = int((start+end)/2)
            else:
                if(x>=a[mid] and x<=a[end]):
                    start=mid+1
                    mid = int((start+end)/2)
                else:
                    end=mid-1
                    mid = int((start+end)/2)
        return 0
        



print("Rotated Right "+str(findRot(a))+" times or " + "Rotated Left "+str(len(a)-findRot(a))+ " times.") 

if(findNum(a,5)):
    print("found")
else:
    print("not found")