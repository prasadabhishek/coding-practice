a=[3,4,2,1,5]
b=a
def sort(a):
    noComp=0
    for j in range(1,len(a)):
        temp=a[j]
        tempPos=j
        for i in range(0,j+1):
            noComp+=1
            if(temp>a[j-i]):
                a[tempPos]=a[j-i]
                a[j-i]=temp
                tempPos-=1
def mincandy():
    sort(a)

mincandy()
for i in range(0,len(a)):
    print(a[i])
