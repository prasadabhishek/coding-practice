import sys

args=[]
f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
for line in f:
    if line.strip():
        line = line.rstrip('\n')
        args = line.split(",")
        bits = bin(int(args[0]))
        if(int(bits[len(bits) - int(args[1])])==int(bits[len(bits) - int(args[2])])):
            print("true")
        else:
            print("false")