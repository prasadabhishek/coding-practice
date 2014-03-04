graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
 
visited=[]

count=0

def findisland(graph,visited,count):
    for i in range(0,len(graph)):
        for j in range(0,len(graph)):
            node=str(i)+str(j)
            if(node not in visited):
                visited.append(node)
                for k in range(0,8):
                    node=str(i+rowNbr[k])+str(j+colNbr[k])
                    if(graph[i][j]==1 and graph[i+rowNbr[k]][j+colNbr[k]] and node not in visited and i+rowNbr[k] >-1 and  i+rowNbr[k] <len(graph) and j+colNbr[k]>-1 and j+colNbr[k]<len(graph)):
                        visited.append(node)
                        count+=1
                        findisland(graph,visited,count)
                    else:
                        break
findisland(graph,visited,count)
print(str(count))