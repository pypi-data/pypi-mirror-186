import json

from ..HTTP.Requests import *

BASE_URL = 'https://www.googleapis.com/gmail/v1/'
OAUTH_BASE_URL = 'https://oauth2.googleapis.com/'

class gmail:

  def __init__(self, client_id, client_secret, refresh_token):
    self.refresh_token = refresh_token
    self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    auth_body = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    auth_url = f"{OAUTH_BASE_URL}token"
    result = post(auth_url, self.headers, json.dumps(auth_body))
    self.access_token = result['content'].get('access_token')
    self.headers['Authorization'] = f"Bearer {self.access_token}"

  def get_auth_headers(self):
    return self.headers

  def get_me(self):
    post_url = f"{BASE_URL}users/me/profile"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve profile. Result: {result}")
    return result

  def watch_me(self, label_ids=None):
    post_url = f"{BASE_URL}users/me/watch"
    post_body = {
        'topicName': 'projects/expressintegrations/topics/gmail',
        'labelIds': label_ids if label_ids else ['INBOX']
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to watch inbox. Result: {result}")
    return result

  def stop_watching_me(self):
    post_url = f"{BASE_URL}users/me/stop"
    result = post(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to stop watching inbox. Result: {result}")
    return result

  def revoke_token(self):
    headers = {
        'Content-type': 'application/x-www-form-urlencoded'
    }
    post_url = f"{OAUTH_BASE_URL}revoke?token={self.refresh_token}"
    result = post(post_url, headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to revoke token. Result: {result}")
    return result

  def get_history_list(self, start_history_id):
    post_url = f"{BASE_URL}users/me/history?startHistoryId={start_history_id}"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve history list. Result: {result}")
    return result

  def get_labels(self):
    post_url = f"{BASE_URL}users/me/labels"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve labels. Result: {result}")
    return result

  def get_message(self, message_id):
    post_url = f"{BASE_URL}users/me/messages/{message_id}?format=full"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve message. Result: {result}")
    return result

  def modify_message(self, message_id, add_label_ids=None, remove_label_ids=None):
    if not add_label_ids and not remove_label_ids:
      raise Exception(f"You must provide either a list of label IDs to add or remove.")
    post_url = f"{BASE_URL}users/me/messages/{message_id}/modify"
    post_body = {}
    if add_label_ids:
      post_body['addLabelIds'] = add_label_ids

    if remove_label_ids:
      post_body['removeLabelIds'] = remove_label_ids
    result = post(post_url, self.headers, json.dumps(post_body))
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to modify message. Result: {result}")
    return result
