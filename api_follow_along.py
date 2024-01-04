# -*- coding: utf-8 -*-
"""API_follow_along.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h21W1HyuDFfnpGq1DBbG7k0FDy60CK58
"""

import requests
import json
from pprint import pprint

# get secret from colab
from google.colab import userdata
token = userdata.get('ghtoken')

# initialize request parameters
url = 'https://api.github.com/user'
headers = {'Authorization': 'Bearer ' + token}

# send request to GitHub
r = requests.get(url, headers=headers)

# print initial responses
print(r.status_code)
print(r.text)

r_json = json.loads(r.text)
pprint(r_json)