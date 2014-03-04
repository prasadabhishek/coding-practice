#frequency of occurence of a word
dictionary={}


a=raw_input("input a string : ")
l = a.split(" ")
list=[]
for i in range(0,len(l)):
    if (l[i] in list):
        continue
    else:
        list.append(l[i])

for i in range(0,len(l)):
    if(not l[i] in dictionary):
        dictionary[list[i]]="1"
    else:
        s=int(dictionary[l[i]])
        s+=1
        dictionary[l[i]]=str(s)

for i in range(0,len(list)):
    print("occurence of : " + list[i] +" : is : " +   dictionary[list[i]])
