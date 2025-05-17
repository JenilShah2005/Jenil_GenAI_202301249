def wordtokenize(sentence):
    tokens=[]
    temp=""
    for x in sentence:
        if(x==" "):
            if(temp!=""):
                tokens.append(temp)
                temp=""
        else:
            if((x>='a' and x<='z') or (x>='A' and x<='Z')):
                temp+=x
            else:
                if temp!="":
                    tokens.append(temp)
                tokens.append(x)
                temp=""
    if temp!="":
        tokens.append(temp)
    return tokens
          