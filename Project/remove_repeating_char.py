A="potato"
list=[]
result =""
for i in range(0,len(A)):
    if(A[i] not in list):
        list.append(A[i])
        result+=A[i]
    else:
        continue
print(result)          