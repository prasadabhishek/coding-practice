def IsPossible(a, n, sum):
    if (n == 1):
        if(sum == abs(a[0])): 
            return  1
        else:
            return 0
    return IsPossible(a, n-1,  sum + a[n-1]) or IsPossible(a, n-1,  sum - a[n-1])

a=[1,2,3]
print(str(IsPossible(a,3,0)))