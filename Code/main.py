import os
import pprint
data_path = "../Data/"
# Function Definitions


# Begin Commands

# Prints Current Dir
# Changes the directory
os.chdir(data_path)

# Reading the file

dataFile = open('adult.data')

content = dataFile.read().splitlines()

# Parse through each line
words = []

# Elements
age = []
workclass = []
fnlwgt = []
education = []
education_num = []
marital_status = []
occupation = []
relationship = []
race = []
sex = []
capital_gain = []
capital_loss = []
hours_per_week = []
native_country = []
money = []

# Dictionaries
d_age = {}
d_workclass = {}
d_fnlwgt = {}
d_education = {}
d_education_num = {}
d_marital_status = {}
d_occupation = {}
d_relationship = {}
d_race = {}
d_sex = {}
d_capital_gain = {}
d_capital_loss = {}
d_hours_per_week = {}
d_native_country = {}
d_money = {}

def addToDictionary(dict, token):
    dict.setdefault(token, 0)
    dict[token] = dict[token] + 1


# For every line within content
for i in range(len(content)):
    # words is the words in every line
    words = (content[i]).split(", ")
    # Finds the frequency of certain jobs
    word_counter = 0
    for word in words:
        if (word_counter == 0):
            age.append(word)
            addToDictionary(d_age, word)
        elif (word_counter == 1):
            workclass.append(word)
            addToDictionary(d_workclass, word)
        elif (word_counter == 2):
            fnlwgt.append(word)
            addToDictionary(d_fnlwgt, word)
        elif (word_counter == 3):
            education.append(word)
            addToDictionary(d_education, word)
        elif (word_counter == 4):
            education_num.append(word)
            addToDictionary(d_education_num, word)
        elif (word_counter == 5):
            marital_status.append(word)
            addToDictionary(d_marital_status, word)
        elif (word_counter == 6):
            occupation.append(word)
            addToDictionary(d_occupation, word)
        elif (word_counter == 7):
            relationship.append(word)
            addToDictionary(d_relationship, word)
        elif (word_counter == 8):
            race.append(word)
            addToDictionary(d_race, word)
        elif (word_counter == 9):
            sex.append(word)
            addToDictionary(d_sex, word)
        elif (word_counter == 10):
            capital_gain.append(word)
            addToDictionary(d_capital_gain, word)
        elif (word_counter == 11):
            capital_loss.append(word)
            addToDictionary(d_capital_loss, word)
        elif (word_counter == 12):
            hours_per_week.append(word)
            addToDictionary(d_hours_per_week, word)
        elif (word_counter == 13):
            native_country.append(word)
            addToDictionary(d_native_country, word)
        elif (word_counter == 14):
            money.append(word)
            addToDictionary(d_money, word)
        else:
            print("Error has occured!\n")
        word_counter += 1
        word_counter = word_counter % 15

print("Frequency of ages")
pprint.pprint(d_age)
print("Work Class:")
pprint.pprint(d_workclass)
#print("fnlwgt:")
#pprint.pprint(d_fnlwgt) # We care about the averages
print("education:")
pprint.pprint(d_education)
print("education_num:")
pprint.pprint(d_education_num)
print("marital_status:")
pprint.pprint(d_marital_status)
print("occupation:")
pprint.pprint(d_occupation)
print("relationship:")
pprint.pprint(d_relationship)
print("race:")
pprint.pprint(d_race)
print("sex:")
pprint.pprint(d_sex)
#print("capital_gain:")
#pprint.pprint(d_capital_gain)
#print("capital_loss:")
#pprint.pprint(d_capital_loss)
#print("hours_per_week:")
#pprint.pprint(d_hours_per_week)
#print("native_country:")
#pprint.pprint(d_native_country)
print("Made over 50k:")
pprint.pprint(d_money)
