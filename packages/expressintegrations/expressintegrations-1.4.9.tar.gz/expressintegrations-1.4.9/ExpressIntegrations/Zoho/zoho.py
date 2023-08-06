from ..HTTP.Requests import *
from ..Utils import Utils

HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}
AUTH_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
AUTH_URL = 'https://accounts.zoho.com'
BASE_URL = 'https://books.zoho.com/api/v3/{}?organization_id='
CONFIG = {}


def authenticate(force=False):
  if CONFIG['expires_at'] is None or CONFIG['expires_at'] < Utils.now() or force:
    post_url = f"{AUTH_URL}/oauth/v2/token"
    auth_body = {
        'grant_type': 'refresh_token',
        'client_id': CONFIG['client_id'],
        'client_secret': CONFIG['client_secret'],
        'refresh_token': CONFIG['refresh_token']
    }
    result = post(post_url, AUTH_HEADERS, auth_body)
    auth_result = result['content']
    if 'access_token' not in auth_result.keys():
      raise Exception(f"Access token not returned: {result}")
    CONFIG['access_token'] = auth_result['access_token']
    HEADERS['Authorization'] = f"Zoho-oauthtoken {CONFIG['access_token']}"
    CONFIG['expires_at'] = Utils.now() + (auth_result['expires_in'] * 1000)


class zoho:
  import json
  from . import invoices
  from . import contacts
  from . import customerpayments
  from . import users
  from . import items
  from . import expenses

  def __init__(self, auth_data):
    CONFIG['refresh_token'] = auth_data.get('refresh_token')
    CONFIG['access_token'] = auth_data.get('access_token')
    CONFIG['expires_at'] = auth_data.get('expires_at')
    CONFIG['client_id'] = auth_data.get('client_id')
    CONFIG['client_secret'] = auth_data.get('client_secret')
    authenticate()

  # Contains utilities for interacting with the Zoho API

  def get_org_details(self):
    authenticate()
    post_url = f"https://www.zohoapis.com/crm/v2/org"
    HEADERS['Authorization'] = f"Zoho-oauthtoken {self.get_auth_data()['access_token']}"
    return get(post_url, HEADERS)

  def revoke_token(self):
    post_url = f"{AUTH_URL}/oauth/v2/token/revoke?token={CONFIG['refresh_token']}"
    return post(post_url, AUTH_HEADERS)

  def get_auth_data(self):
    return {
        'access_token': CONFIG['access_token'],
        'expires_at': CONFIG['expires_at']
    }
