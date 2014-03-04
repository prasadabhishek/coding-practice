import sys
import gc

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

#list=[]
#f = open(sys.argv[1],"r")
f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
gc.enable()
for line in f:
    if line.strip():
        line = line.rstrip('\n').split(" ")
        string=""
        for j in range(1,int(line[2])+1):
            if(is_divisible(j,int(line[1])) and is_divisible(j,int(line[0]))):
                string+="FB "
            elif(is_divisible(j,int(line[0]))):
                string+="F "
            elif(is_divisible(j,int(line[1]))):
                string+="B "
            else:
                string+=str(j)+" "
    print(string)
f.close()
gc.collect()