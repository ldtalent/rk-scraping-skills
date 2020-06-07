import pandas as pd 

 

def add_skill_manual(df_ld_skill):
    while True:
        
        manual_skill = input("Please enter the skill: ")

        count = 0
        category = df_ld_skill.columns 

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

        df_ld_skill[category_to_add]=df_ld_skill[category_to_add].fillna(manual_skill,limit=1)

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

    return df_ld_skill

