#word break

s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
used =[]
temp=""
sentences=[]
while(len(used)!=len(dict)):
    result=""
    for i in range(0,len(s)):
        temp+=s[i]
        if(temp in dict and temp not in used):
            result+=temp
            used.append(temp)
            temp=""
            if(len(s)-i>1):
                result+=" " 
    if(result not in sentences):  
        sentences.append(result)

