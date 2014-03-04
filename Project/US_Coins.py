#list to store the change values'
denominations=[1,5,10,25,50]
denominations.sort()#sort ascending
list=[]
list2=[]


def computeChange(a,n):
    if(n==0):
        return
    for i in range(len(a)-1,-1,-1): #from highest to lowest denomination
        #can a[i] be used ?
        if(int(n/a[i]) !=0):
            list.append(a[i])
            computeChange(a,n-a[i])
            return

def computeChange2(a,n):
    if(n==0):
        return
    

def computeNumberofCoins(a,n):
    count=0
    for i in range(len(a)-1,-1,-1):
        while (n/a[i]>=1):
            count+=int(n/a[i])
            n=n%a[i]
    return count

computeChange(denominations, 17)
print(list)
#computeChange2(denominations,22)
#print(list2)
print("Count is  : " + str(computeNumberofCoins(denominations,17)))