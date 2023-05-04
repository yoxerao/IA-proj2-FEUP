import pandas as pd
from sklearn.model_selection import train_test_split

def get_data(print_data=False):
    df = pd.read_csv("data/Cancer_Data.csv")
    if 'Unnamed: 32' in df.columns:
        df.drop('Unnamed: 32', axis=1, inplace=True)
    df['diagnosis'].replace(['B', 'M'],[0, 1], inplace=True) # B = 0, M = 1 
    
    #df.drop_duplicates()
    
    if print_data:
        print(df.head())
        print("\n")
        print(df.isnull().sum())
        print("\n")
        print(df.dtypes)
        print("\n")
        description = df.describe()
        for row in description:
            print(description[row])
        print("\n")
        print(df['diagnosis'].value_counts())
    return df
    
get_data(True)




