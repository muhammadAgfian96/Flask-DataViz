import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('mpg')
ori_usa = df['origin'] == 'usa'
ori_jpn = df['origin'] == 'japan'
ori_eur = df['origin'] == 'europe'

def top_3_hp():
    top3_usa = list(df[ori_usa].sort_values(by='horsepower', ascending=False)['name'].head(3))
    top3_jpn = list(df[ori_jpn].sort_values(by='horsepower', ascending=False)['name'].head(3))
    top3_eur = list(df[ori_eur].sort_values(by='horsepower', ascending=False)['name'].head(3))

    data_top={
        'Ranking':['Rank 1', 'Rank 2', 'Rank 3'],
        'usa': top3_usa,
        'japan' : top3_jpn,
        'europe' : top3_eur
    }

    data = pd.DataFrame(data_top, index=['Rank 1', 'Rank 2', 'Rank 3'])
        
    return data

def top_3_irit():
    # mpg besar maka irit
    top3_usa = list(df[ori_usa].sort_values(by='mpg', ascending=False)['name'].head(3))
    top3_jpn = list(df[ori_jpn].sort_values(by='mpg', ascending=False)['name'].head(3))
    top3_eur = list(df[ori_eur].sort_values(by='mpg', ascending=False)['name'].head(3))

    data_top={
        'Ranking':['Rank 1', 'Rank 2', 'Rank 3'],
        'usa': top3_usa,
        'japan' : top3_jpn,
        'europe' : top3_eur,

    }

    data = pd.DataFrame(data_top, index=['Rank 1', 'Rank 2', 'Rank 3'])
        
    return data

    
def lima_data():
    data_all = df
    return data_all.head(5)

def all_data():
    data_all = df
    return data_all