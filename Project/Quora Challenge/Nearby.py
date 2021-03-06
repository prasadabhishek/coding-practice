import math
import time

class location:
     def __init__(self):
         self.topic_number=0
         self.questions=[]
         self.x=0
         self.y=0
     def setLocation(self,x,y,z):
         self.topic_number=x
         self.x=y
         self.y=z
     def getTopicNumber(self):
         return self.topic_number
     def getX(self):
         return float(self.x)
     def getY(self):
         return float(self.y)
     def addQuestion(self,x):
         self.questions.append(x)

class qt_details:
     def __init__(self):
         self.topics=[]
         self.number=0
         self.count=0
     def addTopic(self,x):
         self.topics.append(x)
     def setNumber(self,x):
         self.number=x
     def setCount(self,x):
         self.count=x
     def getTopics(self):
         return self.topics
     def getNumber(self):
         return self.number
     def getCount(self):
         return self.count
        
def calcDist(x1,x2,y1,y2):
    return math.sqrt(math.pow(abs(float(x2)-float(x1)),2) + math.pow(abs(float(y2)-float(y1)),2))

start = time.time()

with open("C://Users//Abhishek//Documents//Visual Studio 2013//Projects//Project//Project//Quora Challenge//coord.txt") as f:
    for line in f:
        line = line.rstrip('\n')
        qtNumbers = line.split(" ")

        topic_details=[]
        for i in range(0,int(qtNumbers[0])):
            line = f.readline()
            co_ordinates = line.rstrip('\n').split(" ")
            co=location()
            co.setLocation(co_ordinates[0],float(co_ordinates[1]),float(co_ordinates[2]))
            topic_details.append(co)

        qt_list=[]
        for i in range(0,int(qtNumbers[1])):
            line = f.readline()
            topics = line.rstrip('\n').split(" ")
            qt=qt_details()
            qt.setNumber(topics[0])
            qt.setCount(topics[1])
            for j in range(2,len(topics)):
                qt.addTopic(topics[j])
            qt_list.append(qt)

        query_list=[]
        for i in range(0,int(qtNumbers[2])):
            line = f.readline()
            line = line.rstrip('\n')
            query_list.append(line)

for i in range(0,int(len(query_list))):
    answer=[]
    query=query_list[i].split(" ")
    if(query[0]=="t" or query[0]=="T"):
        dist_list=[]
        t_list=[]
        dist=0
        for j in range(0,len(topic_details)):
            dist=calcDist(float(query[2]),float(topic_details[i].getX()),float(query[3]),float(topic_details[i].getY()))
            if(len(dist_list)<int(query[1])):
                dist_list.append(dist)
                t_list.append(j)
            else:
                for k in range(0,len(dist_list)):
                    if(dist<dist_list[k]):
                        dist_list[k]=dist
                        t_list[k]=j
        string=""
        for x in range(0,len(t_list)):
            string+=str(t_list[x])+" "
        print(string)
           
    else:
        dist_list=[]
        t_list=[]
        dist=0
        for j in range(0,len(topic_details)):
            dist=calcDist(float(query[2]),float(topic_details[i].getX()),float(query[3]),float(topic_details[i].getY()))
            if(len(dist_list)<int(query[1])):
                dist_list.append(dist)
                t_list.append(j)
            else:
                for k in range(0,len(dist_list)):
                    if(dist<dist_list[k]):
                        dist_list[k]=dist
                        t_list[k]=j
        
        for l in range(int(query[1]),-1,-1):
            for m in range(0,len(t_list)):
                if(str(t_list[m])  in qt_list[l].getTopics()):
                    if(l not in answer):
                        answer.append(l)
        string=""
        for x in range(0,len(answer)):
            string+=str(answer[x])+" "
        print (string)

end = time.time()
print ("Time : " + str(end - start))


