def is_palindrome(word):
    word=word.lower()
    result=""
    for i in word:
        result=i+result
    if result==word:
        return True
    else:
        return False
    
   

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
