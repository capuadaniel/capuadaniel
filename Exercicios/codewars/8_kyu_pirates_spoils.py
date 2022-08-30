#You have 4 inputs:

#spoils total - The value of riches plundered (will be int)
#expenses - The percentage of the spoils_total, before captain_tax is taken out, that is taken for expenses and ship repairs (i.e. expenses = 5 means 5 percent of total spoils were used for expenses)
#captain tax - The amount of money you as captain skim off the top before distributing to your crew
#crew - a table of crew members where keys represent their names and values represent the amount of money they took

def spoils(spoils_total, expenses, captain_tax, crew):
    fools = []  # lista que guarda quem ficou sem dinheiro
    cap_m = 0  # dineheiro inicial do capitão
    total = 0

    for k, v in crew.items():
        grana_crew += v

    grana crew = (100 - captain_tax)
    x = 100
    c = grana_crew *100 - (100 - capitain_tax)

    print(total)
    if cap_m == 0:  # ladrão
        return("Jimmy, Wallace - Walk the plank!")
    elif cap_m >0:  # capitão ladrão
        return(f"Captain needs his gold! Sorry {fools}", )
    else:
        return("Yo-Ho. Yo-Ho. A pirate's life for me!")

#test
crew = {'Wallace': 25, 'Jimmy': 23, 'Petey': 15, 'George': 12}
print(spoils(100, .05, 20, crew), " = Jimmy, Wallace - Walk the plank!")
print(spoils(80, .20, 10, crew), " = Jimmy, Petey, Wallace - Walk the plank!")
print(spoils(1000, .1, 2, crew), " = Captain needs his gold! Sorry George, Jimmy, Petey, Wallace")

crew = {'Wallace': 5, 'Jimmy': 5, 'Petey': 5, 'George': 5}
print(spoils(30, .2, 4, crew), " = Yo-Ho. Yo-Ho. A pirate's life for me!")