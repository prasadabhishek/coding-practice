#Insertion Sort

a=[2,50,11,71,71,65,45,13,98,6]
noComp=0
for j in range(1,len(a)):
    temp=a[j]
    tempPos=j
    for i in range(0,j+1):
        noComp+=1
        if(temp<a[j-i]):
            a[tempPos]=a[j-i]
            a[j-i]=temp
            tempPos-=1
for i in range(0,len(a)):
    print(a[i])

print("\n No. of Comparisons : " + str(noComp))