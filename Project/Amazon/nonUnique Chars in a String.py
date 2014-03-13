str="geeksforgeeks"
list=list(str)
length=len(list)
flag=0
i=0
while(i<length):
    offset = ord(list[i])-ord('a')
    if((flag & (1<<offset))>0):
        for j in range(i,length-1):
            list[j]=list[j+1]
        length=length-1
    else:
        i=i+1
    flag=flag | (1<<offset)
print(list)