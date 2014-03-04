r=5
r1=0
r2=0
r3=0
c=5
c1=0
c2=0
c3=0
sum1=0
sum2=0
sum3=0
max=0

for i in range(0,5):
    c1=i
    c2=i
    c3=i
    while(r1!=r-1 and c1<c-1):
        if(c1-1>=0):
            sum1+=1
            r1+=1
            c1-=1
            if(max<sum1):
                max=sum1
        else:
            break

    while(r2!=r-1 and c2<c-1):
        if(c2>=0):
            sum2+=1
            r2+=1
            if(max<sum2):
                max=sum2
        else:
            break

    while(r3!=r-1 and c3!=c-1):
        if(c3+1<=2):
            sum3+=1
            r3+=1
            c3+=1
            if(max<sum3):
                max=sum3
        else:
            break


print("Max : " +str(max))
