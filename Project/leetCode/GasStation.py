g=[1,1,5,7]
d=[3,3,3,3]

f=list(range(len(g)))
for i in range(0,len(f)):
    f[i]=g[i]-d[i]

list=list(range(len(f)))

while(len(list)!=1):
    i=len(list)-1
    #if(f[0]<=0):
    #    f.pop(0)
    #    list.pop(0)
    #    i-=1
    while(i>-1):
        if(f[i]<=0):
            if(i==0):
                f[len(list)-1]=f[len(list)-1]+f[i]
            f[i-1]=f[i-1]+f[i]
            f.pop(i)
            list.pop(i)
            i-=1
        else:
            i-=1

print("The starting point is GasStation No :" + str(list))