A="aabccddeeff"
xor=0
for i in range(0,len(A)):
    xor=xor^ord(A[i])
print(chr(xor))