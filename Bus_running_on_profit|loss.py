def calculate(distance,no_of_passengers):
   milege=10
   pertrol=distance/milege
   price_petrol=pertrol*70
   profit=(no_of_passengers*80)-price_petrol
   if profit>=0:
       return profit
   else:
        return -1
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
