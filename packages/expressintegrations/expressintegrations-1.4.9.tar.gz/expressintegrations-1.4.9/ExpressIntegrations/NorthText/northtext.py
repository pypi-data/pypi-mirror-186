import requests
import time
from datetime import datetime


class northtext:
  headers = {"Content-Type": "application/json", "Accept": "application/json"}
  base_url = 'https://api.northtext.com'
  access_token = None

  def __init__(
      self,
      access_token=None
  ):
    self.access_token = access_token

    if access_token:
      self.headers['X-API-Key'] = access_token
    else:
      raise Exception('An access token must be provided')

  # Contains utilities for interacting with the Acuity API
  def api_call(self, method, endpoint, data=None):
    r = getattr(requests, method.lower())(url=f"{self.base_url}{endpoint}", data=data, headers=self.headers)
    # rate limiting
    while r.status_code == 429:
      time.sleep(1)
      r = getattr(requests, method.lower())(url=f"{self.base_url}{endpoint}", data=data, headers=self.headers)
    if r.status_code >= 400:
      raise Exception(r.text)
    return r.json()

  def get_messages(self, limit: int = 100, page: int = 0, order: str = 'ASC', contact_id: int = None):
    contact_param = f"&Contact={contact_id}" if contact_id else ''
    return self.api_call('get', f"/api/v2/message?Limit={limit}&Page={page}&Order={order}{contact_param}")

  def send_message(self, data: dict):
    return self.api_call('post', f"/api/v2/message", data=data)

  def get_contacts(
      self,
      limit: int = 100,
      page: int = 0,
      order: str = 'ASC',
      phone_number: str = None,
      since: str = None
  ):
    phone_param = f"&PhoneNumber={phone_number}" if phone_number else ''
    since_param = f"&lastUpdate={since}" if since else ''
    return self.api_call('get', f"/api/v2/contact?Limit={limit}&Page={page}&Order={order}{phone_param}{since_param}")

  def create_contact(self, data: dict):
    return self.api_call('post', f"/api/v2/contact", data=data)

  def get_contact(self, contact_id: int):
    return self.api_call('get', f"/api/v2/contact/{contact_id}")

  def update_contact(self, contact_id: int, data: dict):
    return self.api_call('put', f"/api/v2/contact/{contact_id}", data=data)
