"""### Using previous class' code using TRY/EXCEPT """

import requests
import json
from pprint import pprint
from google.colab import userdata

def get_user_data() -> dict:

  """ Get the authenticated user data object from GitHub.
  Connect to the GitHub API and retrieve the authenticated users' data as Python dictionary.
  The token is retrieved from the colab userdata system.

  Parameters
  ----------
  None

  Returns
  -------
  user_obj : dict
    User data retrieved from GitHub

  Examples
  --------
  user_obj = get_user_data()
  pprint(user_obj)

  {
    'name': 'Simeon Wong',
    'login': 'dtxe',
    ...
  }
  """

  token = userdata.get('ghtoken')

  main_api = 'https://aasdsasadaapi.com'
  backup_api = 'https://api.github.com'

  try:
    # get response from first API
    response = requests.get(url=main_api+'/user',
                          headers={'Authorization': 'Bearer ' + token})
    print('success from first API')

  except requests.exceptions.ConnectionError:
    print('Error with 1st API, trying 2nd')
    # connection error to first API, let's try backup
    response = requests.get(url=backup_api+'/user',
                          headers={'Authorization': 'Bearer ' + token})
    print('Success from 2nd API')

  # parse json
  # response_json = json.loads(response.text)

  return response.json()

user_obj = get_user_data()

pprint(user_obj)

# print some values
#print('Username: ' + user_obj['login'])
#print('Name: ' + user_obj['name'])