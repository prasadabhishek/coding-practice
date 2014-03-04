import sys

f = open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//Yodle//triangle.txt","r")

list=[]
for line in f:
    if line.strip():
        line = line.rstrip('\n').split(" ")
        if("" in line):
            line.remove("")
        line=[int(i) for i in line]
        list.append(line)


for i in range((len(list)-2),-1,-1):
    for j in range(0,len(list[i])):
        list[i][j]+=max(list[i+1][j],list[i+1][j+1])
print(str(list[i][0]))