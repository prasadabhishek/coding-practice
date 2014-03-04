import sys

f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
for line in f:
    if line.strip():
        string=""
        line = line.rstrip('\n')
        for i in range(0,len(line)):
            if((ord(line[i])>64 and ord(line[i])<91) or (ord(line[i])>96 and ord(line[i])<123)):
                if(ord(line[i])<97):
                    string+=chr(ord(line[i]) + 32)
                else:
                    string+=line[i]
            else:
                string+=line[i]
        print(string)
        