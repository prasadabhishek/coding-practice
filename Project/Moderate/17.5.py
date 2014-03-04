#game of master mind

a = ["" for x in xrange(4)]
b = ["" for x in xrange(4)]
c=[]
for i in range (0,4):
    a[i]=raw_input("Enter correct Value for slot : " +str(i)+" : ")
for i in range (0,4):
    b[i]=raw_input("Enter guess Value for slot : " +str(i)+" : ")

    hitcount=0
    phitcount=0
for i in range (0,4):
    for j in range(0,4):
        if (i==j and b[i]==a[j]):
            if(b[i] in c):
                phitcount-=1
            else:
                c.append(b[i])
            hitcount+=1
        if (b[i]==a[j] and not(b[i] in c)):
            phitcount+=1
            c.append(b[i])
print("Hit Count = "+str(hitcount))
print("Psuedo Hit Count = "+str(phitcount))