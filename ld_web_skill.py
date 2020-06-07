from bs4 import BeautifulSoup
from selenium import webdriver 
import pandas as pd 


def get_skills():

    driver = webdriver.Firefox()

    main_url = 'https://www.learningdollars.com/client/select_engineers/'

    driver.get(main_url)

    soup = BeautifulSoup(driver.page_source,'lxml')    
    
    category_list=driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/form/div[1]/div[1]/div/select/option')
    
    category = []

    skills = []

    for item in category_list: 

        category.append(item.text)

        skills_list = []

        item.click()

        skills_list=driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/form/div[1]/div[2]/div/select/option')

        skills.append([i.text for i in skills_list])
        
    driver.close()

    category_skill = {}

    count = 0
    for i in category:
        if count == 0:
            category_skill[i] = sorted(skills[count])
        else:
            skill_1 = set(skills[count])
            skill_2 = set(skills[count - 1])
            skill_final = skill_1-skill_2
            category_skill[i] = sorted(list(skill_final))
        count = count + 1

    
    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in category_skill.items() ])) 

    df.to_csv("LD_site_data.csv")

    return df




