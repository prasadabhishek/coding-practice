#text="{hey what is{up}}"


def check(text):
    stack=[]
    for i in range(0,len(text)):
        if(text[i]=='{' or text[i]=='(' or text[i]=='<' or text[i]=='['):
            stack.append(text[i])
        else:
            if(text[i]=='}' or text[i]==')' or text[i]=='>' or text[i]==']'):
                c=stack.pop()
                if((text[i]=='}' and c=='{') or (text[i]==')' and c=='(') or (text[i]=='>' and c=='<') or  (text[i]==']' and c=='[')):
                    continue
                else:
                    return 0
            else:
                continue
    if(len(stack)==0):
        return 1
    else:
        return 0

text =input("Enter a stream : ")
if(check(text)):
    print("Correct Parentheses")
else:
    print("wrong")