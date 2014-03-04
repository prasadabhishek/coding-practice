#determine if a string has all unique characters
s="abcde"
flag=0
for i in range(0,len(s)):
    temp=s[i]
    for j in range(0,len(s)):
        if(i!=j):
            if(s[j]==temp):
                flag=1
                break
if(flag==0):
    print("UNIQUE")
else:
    print("NOT UNIQUE")