a=[1,2,3,4,5,6,7,8,9]
d=3
temp=0
for i in range(0,len(a)-d):
    if(i<=int(len(a)/2)):
         temp=a[i]
         a[i]=a[i+d]
         a[i+d]=temp
    else:
        temp=a[i]
        a[i]=a[len(a)-1]
        a[len(a)-1]=temp
print(a)