import math

A=[1,2,2,3,3,4,5,5,6,6,7]
xor=0
for i in range(0,len(A)):
    xor=xor^A[i]
set_bit= xor & ~(xor-1)

x=0
y=0

for i in range(0,len(A)):
    if(A[i] & set_bit!=0):
        x = x ^ A[i]
    else:
        y = y ^ A[i]


print("The first number is : " + str(x))
print("The second number is : " + str(y))