def find_winner_of_the_day(*match_tuple):
    count1=0
    count2=0
    team1="Team1"
    team2="Team2"
    tie="Tie"#Remove pass and write the logic here
    for i in match_tuple:
        if i=="Team1":
            count1+=1
        elif i=="Team2":
            count2+=1
        else:
            pass
    if count2>count1:
        return team2
    elif count1>count2:
        return team1
    elif count1==count2:
        return tie
    else:
        pass
       
print(find_winner_of_the_day("Team1","Team2","Team1","Team2","Team2"))
