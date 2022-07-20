import numpy as np
def medal_tally(df,year,country):
        medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Games', 'Sport', 'Event', 'Medal'])

        flag = 0
        if year == 'OverAll' and country == 'OverAll':
            tem_df = medal_df

        if year == 'OverAll' and country != 'OverAll':
            flag = 1
            tem_df = medal_df[medal_df['region'] == country]

        if year != 'OverAll' and country == 'OverAll':
            tem_df = medal_df[medal_df['Year'] == int(year)]

        if year != 'OverAll' and country != 'OverAll':
            tem_df = medal_df[(medal_df['region'] == country) & (medal_df['Year'] == int(year))]
        if flag == 1:
            x = tem_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
        else:
            x = tem_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                         ascending=False).reset_index()

        x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']
        x['Total']=x['Total'].astype(int)
        x['Gold']=x['Gold'].astype(int)
        x['Silver']=x['Silver'].astype(int)
        x['Bronze']=x['Bronze'].astype(int)

        return x
def country_years_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'OverAll')
    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0,'OverAll')
    return years,countries
def data_over_time(df,col,y_axis):
    overall_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values(
        'index')
    overall_time.rename(columns={'index': 'Year', 'Year': y_axis}, inplace=True)
    return overall_time


def most_succ(df, sport):
    temp_df = df.dropna(subset=['Medal'])
    if sport != 'OverAll':
        temp_df = temp_df[temp_df['Sport'] == sport]
        x = temp_df['Name'].value_counts().head(15).reset_index().merge(df, left_on='index', right_on='Name', how='left')[
            ['index',
             'Name_x', 'Sport', 'region']].drop_duplicates('index')
        x.rename(columns={'index': 'Name', 'Name_x': 'Medal', 'region': 'Country'}, inplace=True)
        return x
    else:

        x =temp_df['Name'].value_counts().head(15).reset_index().merge(df, left_on='index', right_on='Name', how='left')[
            ['index',
             'Name_x', 'Sport', 'region']].drop_duplicates('index')
        x.rename(columns={'index': 'Name', 'Name_x': 'Medal', 'region': 'Country'}, inplace=True)
        return x
def year_wise(df,country):
    country_df = df.dropna(subset=['Medal'])
    country_df = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Games', 'Sport', 'Event', 'Medal'])
    temp = country_df[country_df['region'] == country]
    country_name = temp.groupby('Year').count()['Medal'].reset_index()
    return country_name
def country_event_heatmap(df,country):
    country_df = df.dropna(subset=['Medal'])
    country_df = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Games', 'Sport', 'Event', 'Medal'])
    temp = country_df[country_df['region'] == country]
    pt=temp.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0)
    return pt
def most_succ_athlete(df,country):
    temp_df=df.dropna(subset=['Medal'])
    temp_df=temp_df[temp_df['region']==country]
    x=temp_df['Name'].value_counts().head(10).reset_index().merge(df,left_on='index',right_on='Name',how='left')[['index',
                                                                                                                          'Name_x','Sport']].drop_duplicates('index')
    x.rename(columns={'index':'Name','Name_x':'Medal','region':'Country'},inplace=True)
    return x
def weight_v_height(df,sports):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sports !='OverAll':
        temp_sport = athlete_df[athlete_df['Sport'] == sports]
        return temp_sport
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    female = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
    final = men.merge(female, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)
    final.fillna(0, inplace=True)
    return final








    
