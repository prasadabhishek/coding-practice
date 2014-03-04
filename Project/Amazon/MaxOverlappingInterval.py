interval=[1,5,1,7,2,3,3,11]
for i in range(0,len(interval)):
    if((i%2)==0):
        dead.append(interval[i])
    else:
        alive.append(interval[i])

alive.sort()
dead.sort()

start=0
end=0
max=0

for i in range(0,max(interval)):
    if(i in alive):
        max+=1
        