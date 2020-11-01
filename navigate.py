from selenium import webdriver
from selenium.common import exceptions
import pandas as pd


api_list = []
category = []
follow = []

browser = webdriver.Firefox()
browser.get('https://www.programmableweb.com/category/all/apis?page=878')
api_skills = browser.find_elements_by_class_name('odd')
for api in api_skills:
    api_name = api.find_element_by_css_selector('td.views-field.views-field-pw-version-title').text
    categories = api.find_element_by_css_selector('td.views-field.views-field-field-article-primary-category').text
    followers = api.find_element_by_css_selector('td.views-field.views-field-flag-follow-api-count').text

    api_list.append(api_name)
    category.append(categories)
    follow.append(followers)
    # browser.find_element_by_xpath("//a[@title='Go to next page']").click()

df = pd.DataFrame(list(zip(api_list,category,follow)), columns=['API_Name','Category','Followers'])
df.to_csv('Final.csv',index=False)
