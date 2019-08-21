def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
def find_strong_numbers(num_list):
    result=0
    rem=0
    temp=0
    strong_num_list=[]
    for i in num_list:
        temp=i
        while(i!=0):
            rem=i%10
            
            result=result+factorial(rem)
            i=i//10
        
            if(result==temp ):
                strong_num_list.append(result)
                result=0
    return strong_num_list
        

num_list=[2, 10, 40585, 0,145]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
