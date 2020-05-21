import pandas as pd

from all_parameter import get_site_data
from getting_data import get_data

#getting all the api_parameters from the api
parameter = get_site_data('https://api.stackexchange.com/2.2/sites?pagesize=500')
#list of api_paramter to remove 
parameter_to_remove = ['gaming', 'cooking', 'photo', 'diy', 'english', 'bicycles', 'rpg', 'boardgames', 'writing', 'scifi', 'skeptics', 'fitness', 'parenting', 'music', 'german', 'japanese', 'judaism', 'christianity', 'philosophy', 'gardening', 'travel', 'french', 'hermeneutics', 'history', 'spanish', 'bricks', 'scicomp', 'movies', 'chinese', 'poker', 'outdoors', 'martialarts', 'sports', 'academia', 'workplace', 'windowsphone', 'chess', 'russian', 'islam', 'patents', 'politics', 'anime', 'genealogy', 'ell', 'sound', 'pets', 'ham', 'italian', 'pt.stackoverflow', 'ebooks', 'alcohol', 'cs50', 'expatriates', 'matheducators', 'puzzling', 'craftcms', 'buddhism', 'hinduism', 'communitybuilding', 'worldbuilding', 'ja.stackoverflow', 'hsm', 'lifehacks', 'coffee', 'musicfans', 'woodworking', 'civicrm', 'ru.stackoverflow', 'rus', 'mythology', 'portuguese', 'es.stackoverflow', '3dprinting', 'latin', 'crafts', 'korean', 'retrocomputing', 'monero', 'esperanto', 'sitecore', 'literature', 'vegetarianism', 'ukrainian', 'cseducators', 'interpersonal', 'iota', 'stellar', 'conlang', 'eosio', 'tezos', 'drones', 'earthscience']



parameter_removed = []
parameter_not_removed = []

for i in parameter:
    if (i in parameter_to_remove) or ('meta' in i):
        parameter_removed.append(i)
    else:
        parameter_not_removed.append(i)




main_df = pd.DataFrame(columns=['name','count'])
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

        main_df = pd.concat([main_df,df], sort=False)



    print("Finished scraping:",api_parameter )


main_df.to_csv('all_data.csv')

            

