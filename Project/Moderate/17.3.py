#trailing zeros in n factorial

def fact(n):
    if(n<=1):
        return n
    else:
        return n * (fact(n-1))

n=input("enter a number : ")
print(str(fact(n)))
f=fact(n)
count=0
while(f%10 ==0):
    f=int(f/10)
    count+=1

print(str(count))
