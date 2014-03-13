import queue

a=[8,1,7,6,0]
a.sort()

q1=queue.Queue(maxsize=len(a))
q2=queue.Queue(maxsize=len(a))
q3=queue.Queue(maxsize=len(a))

sum=0
for i in range(0,len(a)):
    sum=sum+a[i]
    if(a[i]%3==0):
        q1.put(a[i])
    elif(a[i]%3==1):
        q2.put(a[i])
    else:
        q3.put(a[i])

list=[]
if(sum%3==0):
    for i in range(0,q3.qsize()):
        list.append(q3.get())
    list.sort(reverse=True)
    print(list)

if(sum%3==1):
    q2.get()
    if(q2.empty()): 
        if(q3.qsize>2):
            for i in range(0,2):
                q3.get()
        else:
            print("NOT Possible ")
if(sum%3==2):
    q3.get()
    if(q3.empty()): 
        if(q2.qsize>2):
            for i in range(0,2):
                q2.get()
        else:
            print("NOT Possible ")

list=[]
for i in range(0,q1.qsize()):
    list.append(q1.get())
for i in range(0,q2.qsize()):
    list.append(q2.get())
for i in range(0,q3.qsize()):
    list.append(q3.get())

list.sort(reverse =True)
print(list)
