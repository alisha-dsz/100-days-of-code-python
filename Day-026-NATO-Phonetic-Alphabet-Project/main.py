import pandas as pd

#TODO 1. Create a dictionary in this format:

data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = str(input("Enter a word:")).upper()
nato_list = [value for letter in user_input for (key,value) in nato_dict.items() if letter == key]
print(nato_list)
