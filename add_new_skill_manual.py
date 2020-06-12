import pandas as pd 
import numpy as np

from clean_data import wrangle_string_ld

def check_if_skill_exist(ld_skill,manual_skill):
    #Checking if skills exists already
        
    skill_ld_list = []
    for colname,values in ld_skill.iterrows():
        skill_ld_list.append(values)

    skill_series = np.array(skill_ld_list).flatten()

    prior_skill_list = pd.DataFrame(skill_series,columns =["Skill"])

    prior_skill_list['Skill'] = prior_skill_list['Skill'].apply(wrangle_string_ld)
    
    prior_skill_list= list(prior_skill_list['Skill'])

    if str(manual_skill).title() in prior_skill_list:
        print("Skill already exists.")
        return 0 



def add_skill_manual(ld_skill):
    while True:
        
        manual_skill = input("Please enter the skill: ")
        
        skill_exist_checkpoint = check_if_skill_exist(ld_skill,manual_skill)

        if skill_exist_checkpoint == 0:
            continue 
       


        count = 0
        category = ld_skill.columns 

        for i in category:
            skill_no = count+1           
            print("Enter ", skill_no, " to add the skills to ", category[count])
            count = count + 1 
            


        while True:
            try:
                skill_to_add_category = int(input("Please enter the number: "))
                break
            except:
                print("Please enter a number")
                continue

        category_to_add = category[skill_to_add_category - 1]

        ld_skill[category_to_add]=ld_skill[category_to_add].fillna(manual_skill,limit=1)

        while True: 
            answer = input("Do you want to add more skill? (y/n): ")
            if (answer.lower() == 'y') or (answer.lower() == 'n'):
                break
            else:
                print("Invalid option")

        if answer.lower() == 'y':
            continue
        else:
            break 

    return ld_skill

