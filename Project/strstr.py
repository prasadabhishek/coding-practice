#strstr funciton

def strstr(part,whole):
    i=0
    j=0
    count=0
    while i < len(whole):
        temp=i
        count=0
        if(whole[i] in part):
            while j <len(part):
                if(whole[i]==part[j]):
                    count+=1
                    i+=1
                else:
                    break
                j+=1
            i=temp
            j=0
            if(count==len(part)):
                return temp
        i+=1       
                
str1="is"
str2="Abhishek"
pos = strstr(str1,str2)
print(str1 + " is at postion " + str(pos)+" in " + str2)
