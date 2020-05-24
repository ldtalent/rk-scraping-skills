import pandas as pd

from ld_web_skill import get_skills

def remove_num(skill):
    if any(char.isdigit() for char in str(skill)):
        return "Null"
    else:
        return skill

def wrangle_string(skill):
    skill = str(skill).replace("-", " ")
    return str(skill)

def wrangle_string_ld(skill):
    return str(skill).title()

def compare_with_older(skill):
    if str(skill).title() in skill_compare_list:
        print(str(skill) + " is dropped.")
        return "Null"
    else:
        return skill

def clean_main_data(df):
    df=df[['name','count','skills']]
    df = df.drop_duplicates(subset='name')
    df['name']=df['name'].apply(remove_num)
    df = df[df['name'] != "Null"]
    df['name'] = df['name'].apply(wrangle_string)
    df2 = get_skills()
    df2 = df2[['Skill']]
    df2['Skill'] = df2['Skill'].apply(wrangle_string_ld)
    global skill_compare_list
    skill_compare_list= list(df2['Skill'])
    df['name'] = df['name'].apply(compare_with_older)
    df = df[df['name'] != "Null"]
    df.rename(columns={"name": "skill", "skills": "site"})    
    return df
    
