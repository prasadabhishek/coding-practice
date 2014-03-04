import sys

def multiple(x,y):
    i=1
    m=0
    if(x>y):
        return x
    while(m<y):
        m=x*i
        i+=1
    return m

f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
for line in f:
    if line.strip():
        string=""
        line = line.rstrip('\n')
        args = line.split(",")
        print(str(multiple(int(args[1]),int(args[0]))))