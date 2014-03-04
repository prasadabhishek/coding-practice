a=[1,3,3,4,4]
temp=0
for i in range (0,len(a)):
    temp=abs((int)(a[i]));
    temp-=1         
    if(a[temp]>0):
        a[temp]*=-1

for i in range (0,len(a)):
    if(a[i] > 0): 
        print(str(i+1)+"\t"+"\n")