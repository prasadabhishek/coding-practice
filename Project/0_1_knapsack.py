

w=[2,3,4,5]
v=[3,4,5,6]
c=5
max=c+1
knapsack =[[0]*max for x in range(len(w)+1)]
list=[]

for i in range(0,len(w)):
    for j in range(0,max):
        if(j<w[i]):
            knapsack[i+1][j]=knapsack[i][j]
        else:
            knapsack[i+1][j]=v[i]+knapsack[i][j-w[i]]
            if(knapsack[i+1][j] < knapsack[i][j]):
                knapsack[i+1][j] = knapsack[i][j]

k=c
for i in range(len(w),0,-1):
    if (knapsack[i][k] != knapsack[i-1][k] ):
        list.append(i)
        k=k-w[i-1]

print(" The items to be included are : " + str(list) + " the Maximized sum is : " + str(knapsack[len(w)][c]))