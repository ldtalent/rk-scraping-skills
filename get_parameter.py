import json
import pandas as pd

df = pd.DataFrame()

parameter = []
url = []

with open("sites.json", encoding="utf8") as json_file:
    data = json.load(json_file) 
    print(len(data['items']))  
    for i in range(len(data['items'])):        
        parameter.append(data['items'][i]['api_site_parameter'])
        url.append(data['items'][i]['site_url'])

df['Parameter'] = parameter
df['url'] = url

df.to_csv('api_parameter.csv')
            

