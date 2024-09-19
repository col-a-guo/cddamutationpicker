import pandas as pd
import random
import numpy as np

df = pd.read_csv("cddamutations.csv")

mutantcategories = ["Alpha", "Frog", "Beast", "Bird", "Cattle", "Cephalopod", "Chimera", "Chiropteran", "Crustacean", 
                    "Elf-A", "Feline", "Fish", "Snail", "Insect", "Lizard", "Lupine", "Medical", "Mouse", "null", "Plant", 
                    "Rabbit", "Raptor", "Rat", "Slime", "Spider", "Trogolobite", "Ursine"]
#null is mycus

focus_category = "Feline"
focus_weight = 30

#MUTATION VARS
stdev = 2
max = 5
min = -5
mean = 0
stdev = 2
rate = 3


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
        if int(row[1]) in pointrange:
            rand = np.random.normal(mean,stdev)
            if abs(rand-int(row[1])) < 0.5:
                mutation_options.append(row[0])
                if current_name == focus_category:
                    print("focused: "+ row[0])
                    for i in range(focus_weight):
                        mutation_options.append(row[0])

for i in range(rate):
    rand_mutation = random.randint(0,len(mutation_options))
    print(mutation_options[rand_mutation])