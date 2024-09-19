import pandas as pd
import random
import numpy as np
import ast

char_mutations = pd.read_csv("charmutations.csv")
df = pd.read_csv("cddamutations.csv")

mutantcategories = ["Alpha", "Frog", "Beast", "Bird", "Cattle", "Cephalopod", "Chimera", "Chiropteran", "Crustacean", 
                    "Elf-A", "Feline", "Fish", "Snail", "Insect", "Lizard", "Lupine", "Medical", "Mouse", "null", "Plant", 
                    "Rabbit", "Raptor", "Rat", "Slime", "Spider", "Trogolobite", "Ursine"]
#null is mycus

#CHARACTER VARS
focus_category = "Feline"
focus_weight = 30
character = "asdff"

#MUTATION VARS
stdev = 2
max = 5
min = -5
mean = 0
stdev = 2
rate = 10
if not (character in char_mutations["Character"]):
    char_mutations = char_mutations.append({"Character":character, "Mutations":["Human"]}, ignore_index=True)

if type(char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0]) == str:
    char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0] = ast.literal_eval(char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0])
current_char = char_mutations.loc[char_mutations['Character'] == character]
pointrange = [i for i in range(min,max+1)]
current_name = ""
stage = "Pre-Threshold"
mutation_options = []
for index, row in df.iterrows():
    if row[0][-6:-1] == "Prime":
        current_name = row[0][:-7]
        stage = "Pre-Threshold"
    elif row[0] == "Post-Threshold Mutations":
        stage = "Pre-Threshold"
    else:
        if row[0] in current_char["Mutations"] or (row[1] not in pointrange):
            for point_pointer in range(0,6):
                try:
                    print(row[3+i*2])
                    if int(row[3+i*2]) in pointrange:
                        print("advanced mutation woohooo")
                        rand = np.random.normal(mean,stdev)
                        if abs(rand-int(row[1])) < 0.5:
                            mutation_options.append(row[0])
                            if current_name == focus_category:
                                print("focused: "+ row[0])
                                for i in range(focus_weight):
                                    mutation_options.append(row[0])
                except:
                    pass
        elif row[1] in pointrange:
            rand = np.random.normal(mean,stdev)
            if abs(rand-int(row[1])) < 0.5:
                mutation_options.append(row[0])
                if current_name == focus_category:
                    print("focused: "+ row[0])
                    for i in range(focus_weight):
                        mutation_options.append(row[0])
current_list = char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0]
if type(current_list) == str:
    current_list = ast.literal_eval(current_list)
for i in range(rate):   
    rand_mutation = random.randint(0,len(mutation_options))
    if mutation_options[rand_mutation] not in current_list:
        current_list.append(mutation_options[rand_mutation])

char_mutations.loc[char_mutations['Character'] == character]["Mutations"].iat[0] = current_list
print(char_mutations)

char_mutations.to_csv("charmutations.csv",index=False)