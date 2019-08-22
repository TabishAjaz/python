def create_largest_number(number_list):
    list1=sorted(number_list)
    sum=""
    for i in  list1:
        sum=str(i)+sum
    return int(sum)
       
        
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
