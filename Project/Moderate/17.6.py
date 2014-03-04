#find indices n-m to sub sort

a=[0 for x in xrange(13)]

for i in range(0,len(a)):
    a[i]=input("Enter element : "+str(i)+" : ")

low=0
high=len(a)-1
select=0
for i in range(0,len(a)):
    if (a[i]<a[i+1]):
        continue
    else:
        for j in range(0,i):
            if(a[i+1]>=a[j]):
                low+=1
    break

for i in xrange(len(a)-1,0,-1):
    if (a[i]>a[i-1]):
        continue
    else:
       for j in xrange(len(a)-1,i-1,-1):
            if(a[i-1]<=a[j]):
                high-=1
    break

print(str(low-1))
print(str(high))