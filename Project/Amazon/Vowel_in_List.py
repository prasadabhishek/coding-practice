a=['a','b','h','i','s','h','e','k']
n=len(a)
for i in range(0,n):
    c=a[i]
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        a.remove(c)
        a.append(c)
        n-=1
print(str(a))