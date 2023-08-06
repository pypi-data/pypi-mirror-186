
import pandas as pd
import json

df = pd.read_csv("cf-remote/List_of_Abbrevations_Main.csv")


# you can simply use the dataframe (df) to read the columns and covert them as a dict and save it as a jSON file
# below is the part
abb_dict = {}
for i, j in df.iterrows():
    abb_dict[j['Unnamed: 0']] = j['List of Abbreviations ']

# now save your dict to JSON
with open("output.json", 'w') as fp:
    json.dump(abb_dict, fp)

# now sload the same json as use it

def Abbreviation(arr):
    """The passing argument should be given in string characters within quotes """
    with open("output.json",) as jfile:
        loaded_dict = json.load(jfile)
        arr1=arr.upper().strip()
        for i,j in loaded_dict.items():
            if i==arr1:
                print(j)
