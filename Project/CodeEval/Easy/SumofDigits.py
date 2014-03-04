import sys

f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
for line in f:
    sum=0
    if line.strip():
        string=""
        line = line.rstrip('\n')
        for i in range(0,len(line)):
            sum=sum+int(line[i])
        print(str(sum))