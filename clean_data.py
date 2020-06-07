import pandas as pd

from ld_web_skill import get_skills

#Cleaning the data
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

def clean_main_data(df_clean):
    #Initializing clean dataframe
    df_clean=df_clean[['name','count','skills']]

    df_clean = df_clean.drop_duplicates(subset='name')

    df_clean['name']=df_clean['name'].apply(remove_num)

    df_clean = df_clean[df_clean['name'] != "Null"]

    df_clean['name'] = df_clean['name'].apply(wrangle_string)

    #Extracting skills from the ld website to compare them
    df_ld_scrape = get_skills()

    skill_ld_list = []
    for colname,values in df_ld_scrape.iterrows():
        skill_ld_list.append(values)

    skill_series = pd.series(skill_ld_list).ravel()

    df_ld_skill = skill_series.to_frame(name = "Skill")

    df_ld_skill['Skill'] = df_ld_skill['Skill'].apply(wrangle_string_ld)

    global skill_compare_list
    skill_compare_list= list(df_ld_skill['Skill'])

    df_clean['name'] = df_clean['name'].apply(compare_with_older)

    df_clean = df_clean[df_clean['name'] != "Null"]

    df_clean.rename(columns={"name": "skill", "skills": "site"})
        
    return df_clean
    
