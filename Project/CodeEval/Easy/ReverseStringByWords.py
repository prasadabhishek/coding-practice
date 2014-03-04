import sys

list=[]
words=[]
f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//CodeEval//Easy//test.txt","r")
for line in f:
    string=""
    if line.strip():
        line = line.rstrip('\n')
        words = line.split(" ")
        words.reverse()
        for i in range(0,len(words)):
            string+=words[i]+" "
    print(string)
        
