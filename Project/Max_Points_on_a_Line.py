import math

def computeRho( x,y, T ):
    return x * math.cos( T )  + y * math.sin( T ) 
     
def maxPoints(A):
    
    if ( len(A) <= 2 ):
        return len(A)
    max_points = 0
    for i in range(0,180):
        theta = i / (180.0 * 3.141592657);
        accumulator=[0]*1000
        for j in range(0,len(A)):
            rho = round( computeRho( A[j][0],A[j][1],theta ) )
            accumulator[ rho ]+=1;
            if ( accumulator[ rho ] > max_points ):
                max_points = accumulator[ rho ]

    return max_points

A=[[1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[2,4],[2,5]]


print("The max points on same line = " + str(maxPoints(A)))
