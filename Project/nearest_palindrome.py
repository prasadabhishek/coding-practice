import math

a=125
b=""
c=""

for i in range(0,int(math.ceil(len(str(a))/2))):
    b+=str(a)[i]
for i in range(len(b)-1,-1,-1):
    b+=b[i]

if(int(str(b))<int(a)):
    for i in range(0,int(len(b)/2)):
        c+=b[i]
    c=str(int(c)+1)
else:
    for i in range(0,int(len(b)/2)):
        c+=b[i]
    c-=1

for i in range(len(c)-1,-1,-1):
    c+=c[i]

if(abs(a-int(c)) < abs(a-int(b))):
    print(c)
else:
    print(b)