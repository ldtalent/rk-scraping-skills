import pandas as pd
from pandas.io.json import json_normalize


from all_parameter import get_site_data
from tags_data import get_tags

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

for api_parameter in parameter_not_removed:


    df = pd.DataFrame()

    if api_parameter == "stackoverflow":
        tags = get_tags(parameter_not_removed,count,api_parameter,5,100)
        tags_2 = get_tags(parameter_not_removed,count,api_parameter,5,100,6)
        if (tags == 0) or (tags_2 == 0):
            print("Skipped ",api_parameter)
            continue
        data=json_normalize(tags['items'])
        data=pd.concat([data, json_normalize(tags_2['items'])], ignore_index=True)
    else:
        tags = get_tags(parameter_not_removed,count, api_parameter)
        data=json_normalize(tags['items'])
        if (tags == 0):
            print("Skipped ",api_parameter)
            continue
        
    count += 1

    df['name']=list(data['name'])
    
    df['count']=list(data['count'])
   
    if api_parameter == "stackoverflow":
        skills= [api_parameter]*1000
    else:
        skills= [api_parameter]*50
    
    df['skills'] =skills
    main_df = pd.concat([main_df,df])

    # if api_parameter == "stackoverflow":
    #     for i in range(1000):
    #         popularity.append(count[i])
    #         skills.append(name[i])
    #         site.append(api_parameter)
    # else:
    #     for i in range(50):
    #         popularity.append(count[i])
    #         skills.append(name[i])
    #         site.append(api_parameter)


    print("Finished scraping:",api_parameter )


main_df.to_csv('all_data.csv')

            

