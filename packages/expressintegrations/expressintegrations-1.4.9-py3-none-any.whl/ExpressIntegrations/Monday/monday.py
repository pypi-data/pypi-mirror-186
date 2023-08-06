from ..HTTP.Requests import *


class monday:
  def __init__(self, api_key):
    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    self.headers['Authorization'] = f"{api_key}"
    self.base_url = 'https://app.managedmissions.com/API'
