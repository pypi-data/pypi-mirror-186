import requests
import json
import os
from mia_api.config_file import APIPATH
from mia_api.utils import response_return

def connect(username: str, password: str):
  tokenpath = APIPATH + '/token'
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
  data = {
    'grant_type': '',
    'username': username,
    'password': password,
    'scope': '',
    'client_id': '',
    'client_secret': ''
    }
  try:
    response = requests.request("POST", tokenpath, headers=headers, data=data)
  except:
    raise Exception("Mia API not responding. Please contact an admin")
  response_return(response)
  os.environ['MIA_API_TOKEN'] = response.json()["access_token"]
  print(username + " succesfully connected to MIA API")
