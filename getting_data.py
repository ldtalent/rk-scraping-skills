from math import ceil
from pandas import json_normalize
import pandas as pd 

from tags_data import get_tags

# Function to make minimum call to the API

def get_data(stack_skills_number,api_parameter,parameter_not_removed,count):

    skill_Scrape=0

    if stack_skills_number <= 100:
        max_page = 1
        size_of_page = stack_skills_number
        page_no = 1
        tags = get_tags(parameter_not_removed,count,api_parameter,max_page,size_of_page,page_no)
        data = json_normalize(tags['items'])
        skill_Scrape = stack_skills_number
    elif (stack_skills_number > 100) and (stack_skills_number <= 500):
        page_no = 1
        max_page = ceil(stack_skills_number/100)
        size_of_page = 100
        skill_Scrape = max_page * size_of_page
        temp = temp - skill_Scrape
        tags = get_tags(parameter_not_removed,count,api_parameter,max_page,size_of_page,page_no)
        data = json_normalize(tags['items'])
    else:
        no_of_call = ceil(stack_skills_number/500)
        page_no = 1
        temp = stack_skills_number
        skill_Scrape = 0
        for i in range(no_of_call):
            if temp > 500:
                max_page = 5
                size_of_page = 100
                skill_Scrape = skill_Scrape + (max_page * size_of_page)
                temp = temp - 500
                
            else:
                max_page = ceil(temp/100)
                size_of_page = 100
                skill_Scrape = skill_Scrape + (max_page * size_of_page)
                temp = temp - skill_Scrape
            if i == 0:
                tags = get_tags(parameter_not_removed,count,api_parameter,max_page,size_of_page,page_no)
                
                if tags == 0:
                    print("Skipped ",api_parameter)
                    return 0
                else:
                    data = json_normalize(tags['items'])
            else:
                tags_2 = get_tags(parameter_not_removed,count,api_parameter,max_page,size_of_page,page_no)
                page_no = page_no + 5
                if tags_2 == 0:
                    print("Skipped ",api_parameter)
                    return 0
                else:
                    data = pd.concat([data, json_normalize(tags_2['items'])], ignore_index=True)

    print("To make as less call to API as possible ", skill_Scrape , " number of skills are scraped from", api_parameter)

    return [data,skill_Scrape]



