from stackapi import StackAPI
import pandas as pd 

SITE = StackAPI('stackoverflow')

tags = SITE.fetch('tags', max_pages=10, page_size = 100)
tags_more = SITE.fetch('tags', max_pages=10, page_size = 100, page=6)


popularity = []
skills = []
tags_list = tags['items']
tags_list_more = tags_more['items']


for tag_dict_number in range(len(tags_list)):
    popularity.append(tags_list[tag_dict_number]['count'])
    skills.append(tags_list[tag_dict_number]['name'])

for tag_dict_number in range(len(tags_list_more)):
    popularity.append(tags_list_more[tag_dict_number]['count'])
    skills.append(tags_list_more[tag_dict_number]['name'])

data = pd.DataFrame() 

data['Popularity'] = popularity
data['Skills'] = skills

data.to_csv('stackoverflow.csv')