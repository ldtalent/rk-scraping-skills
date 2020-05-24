import pandas as pd
import numpy as np

def remove_num(skill):
    if any(char.isdigit() for char in str(skill)):
        return "Null"
    else:
        return skill

def wrangle_string(skill):
    skill = str(skill).replace("-", " ")
    return skill.title()

def compare_with_older(skill,skill_compare_list):
    if str(skill) in skill_compare_list:
        return "Null"
    else:
        return skill

def clean_main_data(df,df2):
    df=df[['name','count','skills']]
    df = df.drop_duplicates(subset='name')
    df['name']=df['name'].apply(remove_num)
    df = df[df['name'] != "Null"]
    df['name'] = df['name'].apply(wrangle_string)
    df2 = df2[['Skill']]
    df2['Skill'] = df2['Skill'].apply(wrangle_string)
    skill_list= df2['Skill'].to_numpy()
    for i in df.index:
        df.loc[i,'name'] = compare_with_older(df.loc[i,'name'],skill_list)
    df = df[df['name'] != "Null"]
    df.rename(columns={"name": "skill", "skills": "site"})
    
    return df
    
