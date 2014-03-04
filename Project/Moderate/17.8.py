#contiguos sequence with largest sum

a=[0 for x in xrange(6)]

for i in range(0,len(a)):
    a[i]=input("Enter element : "+str(i)+" : ")
max=0
for i in xrange(len(a),0,-1):
    for j in range(0,len(a)):
        sum=0
        if(len(a)-j >=i):
            for k in range(0,i):
                sum=sum+a[j+k]
            if(sum>max):
                max=sum

print(max)

