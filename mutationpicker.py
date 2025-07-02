import pandas as pd
import random
import numpy as np
import ast
import sys


char_mutations = pd.read_csv("charmutations.csv")
df = pd.read_csv("cddamutations.csv")

char_id = 5

mutantcategories = ["Alpha", "Frog", "Beast", "Bird", "Cattle", "Cephalopod", "Chimera", "Chiropteran", "Crustacean", 
                    "Elf-A", "Feline", "Fish", "Snail", "Insect", "Lizard", "Lupine", "Medical", "Mouse", "null", "Plant", 
                    "Rabbit", "Raptor", "Rat", "Slime", "Spider", "Trogolobite", "Ursine"]

char_names = "Mal", "Imriska", "Anatoli", "Dr. Michael", "Father Aimen", "Judith Foster", "Dummy"
char_categories = [["Fish", "Medical", "Slime", "null", "Plant"], ["Alpha", "Spider"], ["Feline"], ["Elf-A"], ["Elf-A"], ["Raptor", "Raptor", "Raptor"], ["Lizard"]]
char_stdev = [2.5, 0.5, 0.5, 1, 1, 2.5, 3]
char_max = [7, 3, 3, 4, 8, 9, 7]
char_min = [-4, -2, -2, -8, -3, -4, -7]
char_mean = [0.5, 0, 0, 0.5, 0.5, 2, 0]
char_rate = [10, 2, 4, 4, 4, 6, 20]
#null is mycus

#CHARACTER VARS
focus_categories = char_categories[char_id]
character = char_names[char_id]
focus_weight = 200

#MUTATION VARS
stdev = char_stdev[char_id]
max = char_max[char_id]
min = char_min[char_id]
mean = char_mean[char_id]
rate = char_rate[char_id]

if not character in char_mutations["Character"].values:
    char_mutations = char_mutations.append({"Character":character, "Mutations":["Human"]}, ignore_index=True)

if type(char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0]) == str:
    char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0] = ast.literal_eval(char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0])
current_char = char_mutations.loc[char_mutations['Character'] == character]
pointrange = []
current_name = ""
stage = "Pre-Threshold"
mutation_options = []
for index, row in df.iterrows():
    if row[0][-6:-1] == "Prime":
        current_name = row[0][:-7]
        stage = "Pre-Threshold"
        pointrange = [i for i in range(min,max+1)]
    elif row[0] == "Post-Threshold Mutations":
        stage = "Post-Threshold"
        pointrange = [i for i in range(min-2,max+3)]
        stdev += 1
    else:
        if row[0] in current_char["Mutations"] or (row[1] not in pointrange):
            if stage == "Post-Threshold":
                pointrange = [i for i in range(min-5,max+6)]
                stdev += 2
            for point_pointer in range(1,len(row)//2):
                if isinstance(row[1+point_pointer*2], str) == True:
                    if int(row[1+point_pointer*2]) in pointrange:
                        print("advanced yippie")
                        print(row)
                        rand = np.random.normal(mean,stdev)
                        print(str(abs(rand-int(row[1]))))
                        if abs(rand-int(row[1])) < 3:
                            mutation_options.append(row[0])
                            if current_name in focus_categories:
                                print("focused: "+ row[0])
                                for j in range(focus_weight):
                                    mutation_options.append(row[0])
        elif row[1] in pointrange:
            rand = np.random.normal(mean,stdev)
            if abs(rand-int(row[1])) < 0.5:
                mutation_options.append(row[0])
                if current_name in focus_categories:
                    print("focused: "+ row[0])
                    for i in range(focus_weight):
                        mutation_options.append(row[0])
            
current_list = char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0]     
if type(current_list) == str:
    current_list = ast.literal_eval(current_list)
       
for i in range(rate):   
    rand_mutation = random.randint(0,len(mutation_options)-1)
    if mutation_options[rand_mutation] not in current_list:
        print(str(mutation_options[rand_mutation]))
        current_list.append(mutation_options[rand_mutation])

current_list[0] = "banana"

sub_df = char_mutations.loc[char_mutations['Character'] == character]["Mutations"].copy()
sub_df.iloc[0] = current_list

char_mutations.loc[char_mutations['Character'] == character, "Mutations"] = sub_df
print(char_mutations)

char_mutations.to_csv("charmutations.csv", index=False)