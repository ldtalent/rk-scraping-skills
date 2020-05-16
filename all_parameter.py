import requests
from pandas.io.json import json_normalize

def get_site_data(api_site):

    site_json= requests.get(api_site).json()

    site_data = json_normalize(site_json['items'])

    return list(site_data['api_site_parameter'])

