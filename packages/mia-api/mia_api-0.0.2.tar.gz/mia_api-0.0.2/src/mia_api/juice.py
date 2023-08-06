import requests
import json
import re
import os
from typing import Optional
from urllib.parse import unquote
from mia_api.config_file import APIPATH
from mia_api.utils import response_return
from fastapi import UploadFile

def make(token: str, pythonfile, jsonfile):
  makejuicepath = APIPATH + '/juices/'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  files = [
    ('subs', (os.path.basename(pythonfile.name), open(pythonfile.name, "rb"), 'text/x-python')),
    ('subs', (os.path.basename(jsonfile.name), open(jsonfile.name, "rb"), 'application/json'))
    ]
  response = requests.post(makejuicepath, headers=headers, files=files)
  response_return(response)
  return response.json()

