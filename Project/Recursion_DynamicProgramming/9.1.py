#steps
import math
count=0
Digits = {1,2,3}
def Rec(current,numDigits):
    global count
    if(numDigits==0):
        sum=0
        temp=current
        while(temp!=0):
            sum=sum + (temp%10)
            temp=int(temp/10)
        if(sum==n):
            count+=1
    else:
        for x in Digits:
            Rec(current*10+x, numDigits-1)


n=int(input("Enter the no. of Stairs : "))
max=n
min=math.ceil(int(n/3))
for i in range(min,max+1):
    Rec(0, i)

print("Count : " + str(count))

