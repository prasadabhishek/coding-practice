import math
a="b"

dist = ["browser","bono","bright","bofa"]
#declare the list
distance=[[0 for x in range(len(b)+1)] for x in range(len(a)+1)] #row=a column=b

#initialize first row n collumn
for i in range(0,(len(a)+1)):
    distance[i][0]=i
for i in range(0,(len(b)+1)):
    distance[0][i]=i

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if (a[i-1]==b[j-1]):
            distance[i][j]=distance[i-1][j-1]
        else:
            distance[i][j]=min(distance[i-1][j-1],distance[i-1][j],distance[i][j-1]) + 1

print("Edit Distance = " + str(distance[len(a)][len(b)]))
