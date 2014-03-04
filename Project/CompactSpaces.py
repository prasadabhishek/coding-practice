testString="Abhishek    is a   boy"
flag=0
i=0
result=""
while i < len(testString):
    if(testString[i]==" "):
        flag=1
        result=result+testString[i];
        for j in range(i,len(testString)-1):
            if(testString[j]==" " and flag==1):
                i+=1
            else:
                flag=0
                break
                
    else:
        result=result+testString[i];
        i+=1

print(result )