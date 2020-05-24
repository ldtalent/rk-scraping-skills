from bs4 import BeautifulSoup
from selenium import webdriver 

import pandas as pd 

def get_skills():

    driver = webdriver.Firefox()

    main_url = 'https://www.learningdollars.com/client/select_engineers/'

    driver.get(main_url)

    soup = BeautifulSoup(driver.page_source,'lxml')

    category=[]

    
    
    category_list=driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/form/div[1]/div[1]/div/select/option')
    
    for item in category_list: 

        skills = []

        item.click()

        skills_list=driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[2]/form/div[1]/div[2]/div/select/option')

        skills.append([i.text for i in skills_list])
    driver.close()

    df = pd.DataFrame(skills[0],columns = ['Skill'])    

    df.to_csv('Scrape.csv')
                
