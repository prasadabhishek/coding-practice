strtext = "this is a good day"
strlen=len(strtext)
i=strlen
pos=strlen-1
start=strlen-1
result=""
while(i>0):
    if(pos!=0):
        if(strtext[pos]!=" "):
            pos-=1
        else:
            for j in range(pos+1,start+1):
                result+=strtext[j]
            pos-=1
            start=pos
            result+=" "
        i=pos
for j in range(pos,start+1):
    if(strtext[j]!=" "):
        result+=strtext[j]
print(result.strip())
    
