stack=[]
A="5 1 2 + 4 * + 3 -"

def operation(a,b,op):
    if(op=='+'):
        return a+b
    if(op=='*'):
        return a*b
    if(op=='-'):
        return a-b
    if(op=='/'):
        return a/b

result=0
for i in range(0,len(A)):
    if(A[i]!=" "):
        if(A[i]!='+' and A[i]!='-' and A[i]!='*' and A[i]!='/'):
            stack.append(A[i])
        else:
            b=int(stack.pop())
            a=int(stack.pop())
            result = operation(a,b,A[i])
            stack.append(str(result))
    else:
        continue

print("Result = " + stack[0])