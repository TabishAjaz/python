def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if legs%2!=0:
        print(error_msg)
    elif(heads>=legs):
        print(error_msg)
    else:
        no_legs=heads*2
        rabbit_count=legs-no_legs
        rabbit_count=rabbit_count//2
        chicken_count=heads-rabbit_count
        print(chicken_count, rabbit_count)
    

   
solve(94,36)
