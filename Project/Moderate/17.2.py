#tic-tac-toe win declarer
a = [[0 for x in xrange(3)] for x in xrange(3)] 
for i in range(0,3):
    for j in range(0,3):
        a[i][j] = input("Enter value of " +str(i) +" " +str(j)+ " box : ")

for i in range(0,3):
    for j in range(0,3):
        if(a[i][j]==a[i][j+1] and a[i][j]==a[i][j+2]):
            print(str(a[i][j])+" player WINS !! ")
            break
        if(a[i][j]==a[i+1][j] and a[i][j]==a[i+2][j]):
            print(str(a[i][j])+" player WINS !! ")
            break
        if(a[i][j]==a[i+1][j+1] and a[i][j]==a[i+2][j+2]):
            print(str(a[i][j])+" player WINS !! ")
            break
        break
    break