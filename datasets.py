import pandas as pd  
import numpy as np

stats = pd.DataFrame({"Name": ["Erling halaand","Kylian Mbappe","Harry Kane", "Ousmane dembele", "Julian Alvarez", "Cody gakpo"],
        "League": ["English premier league", "LaLiga","Bundesliga", "League 1","LaLiga","English premier league"],
         "Goals": [21,15,18,17,12,10],
          "Assists": [10, 5, 8,12,8,15]
          })

print(f'All players\n{stats}\n')


#indexing demonstration
#retrieve data from index 2 only   
print(stats.iloc[2])
#print player with the most goals 

print(f'Player with most goals: {stats[["Name", "Goals"]].max()}\n')
#print the table in reverse 
print(stats.iloc[::-1])

#sorting 
#sort the table by name
print(f'\nTable sorted by Name\n{stats.sort_values("Name", ascending=True)}\n')
print(f'Table sorted by most goals:\n{stats.sort_values("Goals", ascending=False)}\n')


#filtering 

print(f"Players with more than 30 goal contribs:\n{stats[(stats["Goals"] + stats["Assists"]) >= 30]}") # print all players with more than 30 goal involvements
print(f"\nKillian Mbappe contribs:\n{stats[stats["Name"] == "Kylian Mbappe"]}")# print all coloumns and rows where name ==  Kylian Mbappe 


#Aggregation
# group all the data by goals scored and sort from highes to lowest
total_goals = stats.groupby("League")["Goals"].sum()
print(f"\nLeague goal rankings:\n{total_goals.sort_values(ascending=False)}")


################################# NP Arrays##################################
goals = np.array([21,15,18,17,12,10])

#get the mean of all the goals
average = goals.mean()

#calculate the sum of all the goals
total = goals.sum()

#get the lowest goals scored
lowest_goals = goals.min()

#get difference between highest and lowest goals scored
diff = goals.max()-lowest_goals

#sort in ascending order
order = goals.sort()

#get more than 15 goals scored
top_scorers = goals[goals > 15]