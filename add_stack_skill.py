import pandas as pd 


def add_skill_stack(main_df, to_add_df):

    for index, row in to_add_df.iterrows():
        while True:
            question = "Do you want to add "+ str(row['name'])+" from "+str(row['skills'])+"? (y/n)"
            answer = input(question)
            if (answer.lower() == 'y') or (answer.lower() == 'n'):
                break
            else:
                print("Invalid option")

        if answer.lower() == 'y':
            count = 0
            category = main_df.columns 

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

            main_df[category_to_add]=main_df[category_to_add].fillna(row['name'],limit=1)

            while True:
                continue_to_add = input("Do you want to add more skill? (y/n)")
                if (continue_to_add.lower() == 'y') or (continue_to_add.lower() == 'n'):
                    break
                else:
                    print("Invalid option")
            if continue_to_add.lower() == 'y':
                continue
            else:
                break

    return main_df

