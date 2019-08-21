def encode(message):
    ch=message[0]
    result=""
    count=0
    message=message+" "
    
    for i in message:

        if i==ch:
            
            count=count+1
       
        else:
            result=result+str(ch)+str(count)
            ch=i
            count=1
    return result

encoded_message=encode("aaabbbccc")
print(encoded_message)
       
