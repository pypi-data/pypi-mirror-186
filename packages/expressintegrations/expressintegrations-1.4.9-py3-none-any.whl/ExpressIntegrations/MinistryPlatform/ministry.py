import json

from ..HTTP.Requests import *
from ..Utils import Utils
from urllib.parse import urlencode
from datetime import datetime


class ministry:
  headers = None
  expires_at = None
  access_token = None
  auth_refreshed = False
  base_url = None

  def __init__(self, site, access_token, expires_at, client_id, client_secret):
    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    self.headers['Authorization'] = f"Bearer {access_token}"
    self.base_url = site
    self.expires_at = expires_at
    self.access_token = access_token
    self.auth_refreshed = False
    if datetime.now().timestamp() > expires_at:
      self.authenticate(client_id, client_secret)
      self.auth_refreshed = True

  def authenticate(self, client_id, client_secret):
    AUTH_HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
    post_url = f"{self.base_url}oauth/connect/token"
    auth_body = {
        'grant_type': 'client_credentials',
        'scope': 'http://www.thinkministry.com/dataplatform/scopes/all',
        'client_id': client_id,
        'client_secret': client_secret
    }
    result = post(post_url, AUTH_HEADERS, auth_body)
    auth_result = result['content']
    self.access_token = auth_result['access_token']
    self.headers['Authorization'] = f"Bearer {self.access_token}"
    self.expires_at = datetime.now().timestamp() + int(auth_result['expires_in'])

  def get_tables(self):
    post_url = f"{self.base_url}tables"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get tables. Result: {result}")
    return result

  def create_record(self, table, record):
    return self.create_records(table, [record])

  def create_records(self, table, records):
    post_url = f"{self.base_url}tables/{table}"
    result = post(post_url, self.headers, json.dumps(records))
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to create record. Result: {result}")
    return result

  def get_record_by_id(self, table, record_id):
    post_url = f"{self.base_url}tables/{table}/{record_id}"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve record. Result: {result}")
    return result

  def search_records(self, table, search_string=None, order_by=None):
    post_url = f"{self.base_url}tables/{table}"
    if search_string is not None:
      sql_filter = {'filter': search_string}
      post_url = f"{post_url}?${urlencode(sql_filter)}"

    if order_by is not None:
      sql_order = {'order_by': order_by}
      post_url = f"{post_url}&${urlencode(sql_order)}"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve records. Result: {result}")
    return result

  def update_record(self, table, record):
    return self.update_records(table, [record])

  def update_records(self, table, records):
    post_url = f"{self.base_url}tables/{table}"
    result = put(post_url, self.headers, json.dumps(records))
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to update record. Result: {result}")
    return result

  def delete_record(self, table, record_id):
    post_url = f"{self.base_url}tables/{table}/{record_id}"
    result = delete(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to delete record. Result: {result}")
    return result
