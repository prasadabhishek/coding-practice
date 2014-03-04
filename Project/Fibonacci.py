def fibbonaci(a,b,max):
    if(a+b<max):
        print(str(a+b) + " ")
        temp=a
        a=b
        b=temp+b  
        fibbonaci(a,b,max)
    else:
        return

a=0
b=1
print(a)
print(b)
fibbonaci(a,b,1000)