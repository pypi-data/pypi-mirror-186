import requests
import time


class emerge:
  headers = None
  environment = ''
  base_url = None
  access_token = None

  def __init__(
      self,
      environment='',
      access_token=None
  ):

    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    self.base_url = 'https://test.intelifi.com/test.usaintel.com/billing_hubspot_webhook'
    self.environment = environment
    self.access_token = access_token
    if self.environment.lower() == 'prod':
      self.base_url = 'https://hbintegration.intelifi.com/HubspotWebhook'

    if access_token:
      self.headers['Authorization'] = f"Basic {access_token}"
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

  def customers(self, start: int = 0, end: int = 100, since: str = ''):
    return self.api_call('get', f"/api/hubspot/customers/{start}/{end}/{since}")

  def customer_billing_info(self, company_id: int, year: int, month: int):
    return self.api_call('get', f"/api/hubspot/billing/{company_id}/{year}/{month}")
