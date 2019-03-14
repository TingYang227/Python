import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
# print(df.head())


# Question 0
def answer_zero():
    return df.iloc[0]

# print(answer_zero())
# print((df.iloc[2]))
# print(df.loc['China'])

# Question 1
# print(df['Gold'])
import numpy as np

def answer_one():
    most_gold = max(df['Gold'])
    return str(df[df['Gold'] == most_gold].index[0])

most_gold = 576
print(df[df['Gold'] == most_gold].index[0])