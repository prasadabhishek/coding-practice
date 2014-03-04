import sys

def fibbonaci(a,b,n,count):
    if(count==n):
        print(str(a+b))
        return count
    while(count!=n):
        temp=a
        a=b
        b=temp+b  
        if(fibbonaci(a,b,n,count+1)==n):
            return count
    


f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
for line in f:
    if line.strip():
        string=""
        line = line.rstrip('\n')
        n=int(line)
        a=0
        b=1
        fibbonaci(a,b,4,1)
