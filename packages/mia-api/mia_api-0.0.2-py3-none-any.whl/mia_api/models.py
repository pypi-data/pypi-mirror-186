import requests
import json
import os
import xarray as xr
import netCDF4
import pandas as pd
from tabulate import tabulate
from typing import Union, List
from datetime import datetime
from mia_api.config_file import APIPATH
from mia_api.utils import response_return

token = os.getenv("MIA_API_TOKEN")

class MIAJuice:
  def __init__(self, name: str, barname: str):
    self.name = name
    self.barname = barname

  def make(self, jsonfile):
    makejuicepath = APIPATH + '/apps/?barname=' + self.barname
    headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer ' + os.getenv("MIA_API_TOKEN")
    }
    files = ('json_file', (os.path.basename(jsonfile.name), open(jsonfile.name, "rb"), 'application/json'))
    response = requests.request("POST", makejuicepath, headers=headers, files=files)
    response_return(response)

  def historical(self, dataset: bool = False):
    getjuicepath = APIPATH + '/bars/juices/get/?barname=' + self.barname + '&juicename=' + self.name + '&operational=false'
    headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer ' + os.getenv("MIA_API_TOKEN")
    }
    response = requests.request("POST", getjuicepath, headers=headers)
    response_return(response)
    if dataset:
      ds = xr.open_dataset(xr.backends.NetCDF4DataStore(netCDF4.Dataset('name', mode = 'r', memory=response.content)))
    else:
      ds = xr.open_dataarray(xr.backends.NetCDF4DataStore(netCDF4.Dataset('name', mode = 'r', memory=response.content)))
    return ds

  def operational(self, rundate: Union[datetime, List[datetime], None] = None, dataset: bool = False):
    getjuicepath = APIPATH + '/bars/juices/get/?barname=' + self.barname + '&juicename=' + self.name + '&operational=true'
    if rundate:
      if type(rundate) == list:
        data = json.dumps([d.isoformat() for d in rundate])
      else:
        data = json.dumps([rundate.isoformat()])
    else:
      data = {}
    headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer ' + os.getenv("MIA_API_TOKEN")
    }
    response = requests.request("POST", getjuicepath, headers=headers, data=data)
    response_return(response)
    if dataset:
      ds = xr.open_dataset(xr.backends.NetCDF4DataStore(netCDF4.Dataset('name', mode = 'r', memory=response.content)))
    else:
      ds = xr.open_dataarray(xr.backends.NetCDF4DataStore(netCDF4.Dataset('name', mode = 'r', memory=response.content)))
    return ds

class MIAJuiceBar:
  def __init__(self, name: str):
    self.name = name

  @staticmethod
  def available_bars():
    availablebarspath = APIPATH + '/users/me/bars'
    headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer ' + os.getenv("MIA_API_TOKEN")
    }
    response = requests.request("GET", availablebarspath, headers=headers)
    response_return(response)
    return response.json()

  def show_menu(self):
    menupath = APIPATH + '/bars/menu?barname=' + self.name + '&html=false'
    headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer ' + os.getenv("MIA_API_TOKEN")
    }
    response = requests.request("GET", menupath, headers=headers)
    response_return(response)
    menu = response.json()
    data = pd.concat([pd.DataFrame.from_dict(m, orient="index") for m in menu])
    print('#' * 40)
    print(tabulate(data, tablefmt="psql"))
    print(f'JuiceBar total juices/fruits: ' + str(data.shape[0]))
    print('#' * 40)

  def get_juice(self, juice_name: str):
    return MIAJuice(name = juice_name, barname = self.name)
