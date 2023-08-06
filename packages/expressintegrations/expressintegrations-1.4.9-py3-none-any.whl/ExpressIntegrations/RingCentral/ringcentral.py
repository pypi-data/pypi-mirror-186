from ringcentral import SDK
import time
import math


BASE_URL = 'https://platform.ringcentral.com'


class ringcentral:
  def __init__(self, client_id, client_secret, username, password, extension, server_url=BASE_URL, auth_data=None):
    rcsdk = SDK(client_id, client_secret, server_url)
    self.platform = rcsdk.platform()
    self.extension = extension
    if auth_data is not None:
      self.platform._auth.set_data(auth_data)

    if not self.platform.logged_in():
      self.platform.login(username, extension, password)

    try:
      self.get_account_details()
    except Exception as e:
      if 'Token not found' in str(e):
        self.platform.login(username, extension, password)
    self.account_id = self.get_account_details().json().id

  # Contains utilities for interacting with the RingCentral api
  def retry(self, method, url, failure_message, query_params=None, payload=None):
    result = None
    try:
      if method.lower() == 'get':
        result = self.platform.get(url, query_params)
      elif method.lower() == 'post':
        result = self.platform.post(url, payload, query_params)
      elif method.lower() == 'put':
        result = self.platform.put(url, payload, query_params)
      elif method.lower() == 'delete':
        result = self.platform.delete(url)
    except Exception as e:
      wait = 64
      error_message = str(e)
      while (
          'Request rate exceeded' in error_message
          or '429' in error_message
      ):
        print(f"retrying. last result: {str(e)} {method} {url} {query_params} {payload}")
        # Keep connection alive every minute
        for i in range(0, math.floor(wait / 32)):
          print(f"Waiting at {i * 32} seconds...")
          time.sleep(32)
        wait = wait * 2 if wait < 1024 else 1024
        try:
          if method.lower() == 'get':
            result = self.platform.get(url, query_params)
          elif method.lower() == 'post':
            result = self.platform.post(url, payload, query_params)
          elif method.lower() == 'put':
            result = self.platform.put(url, payload, query_params)
          elif method.lower() == 'delete':
            result = self.platform.delete(url)
        except Exception as e1:
          error_message = str(e1)
      if result is None or not result.ok:
        raise Exception(f"{failure_message} Result: {result.error() if result is not None else error_message}")
    return result

  def get_auth_data(self):
    return self.platform._auth.data()

  def get_account_details(self, account_id='~'):
    return self.retry(
        'GET',
        f"/restapi/v1.0/account/{account_id}",
        'Failed to get account details.'
    )

  def send_sms(self, sender_number, recipient_number, text, extension='~'):
    post_body = {
        'from': {
            'phoneNumber': sender_number
        },
        'to': [
            {
                'phoneNumber': recipient_number
            }
        ],
        'text': text
    }
    return self.retry(
        'POST',
        f"/restapi/v1.0/account/~/extension/{extension}/sms",
        'Failed to send sms.',
        payload=post_body
    )

  def renew_webhook(self, subscription_id):
    return self.retry(
        'POST',
        f"/restapi/v1.0/subscription/{subscription_id}/renew",
        'Failed to renew webhook.'
    )

  def create_contact(self, contact, dialing_plan=None):
    query_params = {}
    if dialing_plan is not None:
      query_params['dialingPlan'] = dialing_plan
    return self.retry(
        'POST',
        f"/restapi/v1.0/account/~/extension/~/address-book/contact",
        'Failed to create contact.',
        query_params=query_params,
        payload=contact
    )

  def get_contacts(self, starts_with=None, sort_by=None, page=None, per_page=None, phone_number=None):
    query_params = {}
    if starts_with is not None:
      query_params['startsWith'] = starts_with
    if sort_by is not None:
      query_params['sortBy'] = sort_by
    if page is not None:
      query_params['page'] = page
    if per_page is not None:
      query_params['perPage'] = per_page
    if phone_number is not None:
      query_params['phoneNumber'] = phone_number
    return self.retry(
        'GET',
        f"/restapi/v1.0/account/~/extension/~/address-book/contact",
        'Failed to search contacts.',
        query_params=query_params
    )

  def get_contact(self, contact_id):
    return self.retry(
        'GET',
        f"/restapi/v1.0/account/~/extension/~/address-book/contact/{contact_id}",
        'Failed to get contact.'
    )

  def update_contact(self, contact_id, contact, dialing_plan=None):
    query_params = {}
    if dialing_plan is not None:
      query_params['dialingPlan'] = dialing_plan
    return self.retry(
        'PUT',
        f"/restapi/v1.0/account/~/extension/~/address-book/contact/{contact_id}",
        'Failed to update contact.',
        query_params=query_params,
        payload=contact
    )

  def delete_contact(self, contact_id):
    return self.retry(
        'DELETE',
        f"/restapi/v1.0/account/~/extension/~/address-book/contact/{contact_id}",
        'Failed to delete contact.'
    )

  def search_company_directory(self, search_string=None, show_federated=True, extension_type=None, order_by=None, page=None, per_page=None):
    post_body = {}
    if search_string is not None:
      post_body['searchString'] = search_string
    post_body['showFederated'] = show_federated
    if extension_type is not None:
      post_body['extensionType'] = extension_type
    if order_by is not None:
      post_body['orderBy'] = order_by
    if page is not None:
      post_body['page'] = page
    if per_page is not None:
      post_body['perPage'] = per_page
    return self.retry(
        'POST',
        f"/restapi/v1.0/account/~/directory/entries/search",
        'Failed to search company directory.',
        payload=post_body
    )
