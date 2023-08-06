import base64
import requests
import time

from urllib.parse import urlencode

ACUITY_BASE_URI = "https://acuityscheduling.com/api/v1"


class acuity:
  headers = None

  def __init__(
      self,
      access_token=None,
      user_id=None,
      api_key=None
  ):

    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    if access_token:
      self.headers['Authorization'] = f"Bearer {access_token}"
    elif api_key and user_id:
      credentials = f"{user_id}:{api_key}"
      self.headers = {
          'Authorization': f"Basic {base64.b64encode(credentials.encode('UTF-8')).decode('UTF-8')}"
      }
    else:
      raise Exception('An active connection must be provided')

  # Contains utilities for interacting with the Acuity API
  def api_call(self, method, endpoint, data=None):
    r = getattr(requests, method.lower())(url=f"{ACUITY_BASE_URI}{endpoint}", data=data, headers=self.headers)
    # rate limiting
    while r.status_code == 429:
      time.sleep(1)
      r = getattr(requests, method.lower())(url=f"{ACUITY_BASE_URI}{endpoint}", data=data, headers=self.headers)
    if r.status_code >= 400:
      raise Exception(r.text)
    return r.json()

  def me(self):
    return self.api_call('get', '/me')

  def appointment_by_id(self, appointment_id):
    return self.api_call('get', f"/appointments/{appointment_id}")

  def appointments(self, **params):
    return self.api_call('get', f"/appointments?{urlencode(params)}")

  def appointment_addons(self):
    return self.api_call('get', f"/appointment-addons")

  def appointment_types(self):
    return self.api_call('get', f"/appointment-types")

  def calendars(self):
    return self.api_call('get', f"/calendars")

  def certificates(self, **params):
    return self.api_call('get', f"/certificates?{urlencode(params)}")

  def clients(self, **params):
    return self.api_call('get', f"/clients?{urlencode(params)}")
