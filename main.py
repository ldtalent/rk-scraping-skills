import pandas as pd

from all_parameter import get_site_data
from getting_data import get_data
from clean_data import clean_main_data,wrangle_string_ld

from ld_web_skill import get_skills

from add_new_skill_manual import add_skill_manual
from add_stack_skill import add_skill_stack

#Getting skills from ld site

#ld_skills = get_skills()

ld_skills = pd.read_csv("Final_Skill_Data.csv", encoding="utf-8")

main = ld_skills.copy()

#Add skill manually

while True: 
    add_skill = input("Do you want to add skill manually? (y/n): ")
    if (add_skill.lower() == 'y') or (add_skill.lower() == 'n'):
        break
    else:
        print("Invalid option")

if add_skill.lower() == 'y':
    main = add_skill_manual(ld_skills)

#Add skill from stack

while True: 
    add_skill_by_stack = input("Do you want to add skill from stackexchange? (y/n): ")
    if (add_skill_by_stack.lower() == 'y') or (add_skill_by_stack.lower() == 'n'):
        break
    else:
        print("Invalid option")

if add_skill_by_stack.lower() == 'y':
    
    #getting all the api_parameters from the api
    parameter = get_site_data('https://api.stackexchange.com/2.2/sites?pagesize=500')
    #list of api_paramter to remove 
    parameter_to_remove = ['gaming', 'cooking', 'photo', 'diy', 'stackapps' , 'codereview','webapps','codegolf', 'freelancing' ,'materials','bioinformatics','hardwarerecs','law','medicalsciences','vi','engineering','emacs','joomla','aviation','blender','tridion','magento','robotics', 'softwarerecs' , 'economics','languagelearning' , 'english', 'bicycles', 'rpg','homebrew' ,'boardgames', 'writing', 'scifi', 'skeptics', 'fitness', 'parenting', 'music', 'german', 'japanese', 'judaism', 'christianity', 'philosophy', 'gardening', 'travel', 'french', 'hermeneutics', 'history', 'spanish', 'bricks', 'scicomp', 'movies', 'chinese', 'poker', 'outdoors', 'martialarts', 'sports', 'academia', 'workplace', 'windowsphone', 'chess', 'russian', 'islam', 'patents', 'politics', 'anime', 'genealogy', 'ell', 'sound', 'pets', 'ham', 'italian', 'pt.stackoverflow', 'ebooks', 'alcohol', 'cs50', 'expatriates', 'matheducators', 'puzzling', 'craftcms', 'buddhism', 'hinduism', 'communitybuilding', 'worldbuilding', 'ja.stackoverflow', 'hsm', 'lifehacks', 'coffee', 'musicfans', 'woodworking', 'civicrm', 'ru.stackoverflow', 'rus', 'mythology','opensource','tor','opendata','raspberrypi', 'portuguese', 'es.stackoverflow', '3dprinting', 'latin', 'crafts', 'korean', 'retrocomputing', 'monero', 'esperanto', 'sitecore', 'literature', 'vegetarianism', 'ukrainian', 'cseducators', 'interpersonal', 'iota','webapps','apple','android', 'stellar', 'conlang', 'eosio', 'tezos', 'drones', 'earthscience', 'elementaryos']

    parameter_removed = []
    parameter_not_removed = []

    for i in parameter:
        if (i in parameter_to_remove) or ('meta' in i):
            parameter_removed.append(i)
        else:
            parameter_not_removed.append(i)


    scrape_dataframe = pd.DataFrame(columns=['name','count'])
    count = 0

    while True:
        try:
            stack_skills_number=int(input("Please enter the number of skills you want to scrape from stackoverflow: "))
            break
        except:
            print("Please enter an integer value")

    while True:
        try:
            other_skills_number=int(input("Please enter the number of skills you want to scrape from other site except stackoverflow : "))
            break
        except:
            print("Please enter an integer value")

    for api_parameter in parameter_not_removed:


        df = pd.DataFrame()

        if api_parameter == "stackoverflow":      
            result = get_data(stack_skills_number,api_parameter,parameter_not_removed,count)
            if result != 0:
                data= result[0]
        else:
            result = get_data(other_skills_number,api_parameter,parameter_not_removed,count)
            if result != 0:
                data= result[0]
                
            
        count += 1

        if result == 0:
            print("Moving to next api_parameter")
        else:
            
            df['name']=list(data['name'])
            
            df['count']=list(data['count'])
        
            skills= [api_parameter]*df.shape[0]
            
            df['skills'] = skills

            scrape_dataframe = pd.concat([scrape_dataframe,df], sort=False)



        print("Finished scraping:",api_parameter )



    clean_main = clean_main_data(scrape_dataframe)

    clean_main.to_csv("new_data_from_stackexchange.csv")

    #Adding stack skill in category
    main = add_skill_stack(main,clean_main)


for colname,value in main.iteritems():
    main[colname] = main[colname].apply(wrangle_string_ld)

category_skill={}
for colname,values in main.iteritems():
    to_sort_list = [x for x in values.tolist() if str(x).lower() != 'nan']
    category_skill[colname] = sorted(to_sort_list)
    

main = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in category_skill.items() ]))

main.to_csv("Final_Skill_Data.csv",index=False)
