#The samples below consists of function calls for 4 parlors. Function call for each parlor contains a positive integer, representing the number of staff in the parlor, followed by a sequence of uppercase letters.

#Letters in the sequence occur in pairs. The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer. A customer will be serviced if there is an unoccupied staff. No letter will occur in more than one pair.

#Customers who leave without getting service always depart before customers who are currently being serviced. There are at most 20 staff per parlor. Output:

#For each set of inputs, implement the function "simulateParlor" and output a number telling how many customers, if any, walked away. 0 would indicate all customers were serviced.

#Sample Inputs with Expected Answers

#simulateParlor (2, "ABBAJJKZKZ") = 0

#simulateParlor (3, "GACCBDDBAGEE") = 1

#simulateParlor (3, "GACCBGDDBAEE") = 0

#simulateParlor (1, "ABCBCA") = 2

def simulateParlor(n,flow):
    currentList=[]
    waitList=[]
    count=0
    for i in range(0,len(flow)):
        if(flow[i] not in currentList):
            if(flow[i] not in waitList):
                if(len(currentList)<n):
                    currentList.append(flow[i])
                else:
                    waitList.append(flow[i])
            else:
                if(len(currentList)<n):
                    currentList.append(flow[i])
                    waitList.remove(flow[i])
                else:
                    count+=1
        else:
            currentList.remove(flow[i])
    return count


print(str(simulateParlor (2, "ABBAJJKZKZ")))
print(str(simulateParlor (3, "GACCBDDBAGEE")))
print(str(simulateParlor (3, "GACCBGDDBAEE")))
print(str(simulateParlor (1, "ABCBCA")))