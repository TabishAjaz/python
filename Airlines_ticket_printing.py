def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    if(no_of_passengers>=5):
        for i in range(no_of_passengers-5,no_of_passengers):
            a=str(i+101)
            ticket_number_list.append(airline+":"+source[:3]+":"+destination[:3]+":"+a)
    #Write your logic here
    else:
        for i in range(no_of_passengers):
            a=str(i+101)
            ticket_number_list.append(airline+":"+source[:3]+":"+destination[:3]+":"+a)
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Sydney","London",7))
