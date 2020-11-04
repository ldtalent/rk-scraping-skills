from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

browser = webdriver.Firefox()
browser.get('https://www.programmableweb.com/category/all/apis')


api_list = []
category_list = []
followers_list = []
i=0
while i< 10:
    try:
        api_category = browser.find_elements_by_class_name('odd')
        for api in api_category:
            api_name = api.find_element_by_css_selector('td.views-field.views-field-pw-version-title').text
            category = api.find_element_by_css_selector('td.views-field.views-field-field-article-primary-category').text.lstrip('Category\n')
            followers = api.find_element_by_css_selector('td.views-field.views-field-flag-follow-api-count').text
            
            api_list.append(api_name)
            category_list.append(category)
            followers_list.append(followers)

        # browser.find_element_by_xpath("//a[@title='Go to next page']").click()
        # WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Go to next page']")))
        element = browser.find_elements_by_xpath("//a[@title='Go to next page']")
        if len(element) < 1:
            print("No More Pages")
            break
        else:
            WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Go to next page']"))).click()
        # browser.forward()
        i +=1
    except exceptions.StaleElementReferenceException:
        pass

df = pd.DataFrame(list(zip(api_list,category_list,followers_list)), columns=['API_Name','Category','Followers'])

apis = df.to_csv('Final.csv',index=False)