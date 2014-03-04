#Swap a number in place


s=input("Enter a number")
ans=0
t=s
count=0
while(t!=0):
    t=t/10
    count+=1
for i in range(0,count):
    power=1
    for j in range(i+1,count):
        power*=10
    rem=s%10
    s=int(s/10)
    ans+=rem*power

print(ans)