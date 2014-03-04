def kadane(A):
    start=end=0
    max_ending_here = max_so_far = 0
    for x in range(0,len(A)):
        if(A[x]>max_ending_here):
            start=x
        max_ending_here = max([A[x],0,max_ending_here+A[x]])
        if(max_ending_here>max_so_far):
           end=x
        max_so_far = max(max_so_far,max_ending_here)

    print ("Start : " + str(start) + " End : " + str(end) + " Max Sum : " + str(max_so_far))

A = [3, -1, -2, 4, 5]
a=kadane(A) 
print(str(a))