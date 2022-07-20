import pandas as pd

def pre_processor(df,region_df):
    df = df[df['Season'] == 'Summer']
    #merge
    df = df.merge(region_df, on='NOC', how='left')
    #drop_duplicates
    df.drop_duplicates(inplace=True)
    #get-dummies
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
