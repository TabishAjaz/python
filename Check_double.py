def check_double(number):
    double=number*2
    if sorted(str(number))==sorted(str(double)):
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))
