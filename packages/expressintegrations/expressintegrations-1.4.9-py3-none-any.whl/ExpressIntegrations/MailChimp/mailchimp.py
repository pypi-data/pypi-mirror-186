import hashlib
import json

from ..HTTP.Requests import *


class mailchimp:
  def __init__(self, access_token, api_endpoint):
    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    self.headers['Authorization'] = f"OAuth {access_token}"
    self.base_url = f"{api_endpoint}/3.0/"

  # Contains utilities for interacting with the MailChimp api
  def get_account_details(self):
    post_url = f"{self.base_url}"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve account details. Result: {result}")
    return result

  def get_list_member(self, list_id, subscriber_hash):
    post_url = f"{self.base_url}lists/{list_id}/members/{subscriber_hash}"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']) and not Utils.is_not_found(result['status_code']):
      raise Exception(f"Failed to retrieve list member. Result: {result}")
    return result

  def get_list_member_by_email(self, list_id, email):
    subscriber_hash = hashlib.md5(email.encode()).hexdigest()
    post_url = f"{self.base_url}lists/{list_id}/members/{subscriber_hash}"
    result = get(post_url, self.headers)
    if not Utils.is_success(result['status_code']) and not Utils.is_not_found(result['status_code']):
      raise Exception(f"Failed to retrieve list member. Result: {result}")
    return result

  def create_list_member(self, list_id, email, status, merge_fields=None):
    post_url = f"{self.base_url}lists/{list_id}/members"
    post_body = {
        'email_address': email,
        'status': status,
        'merge_fields': merge_fields
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to create list member. Result: {result}")
    return result

  def update_list_member(self, list_id, subscriber_hash, email=None, status=None, merge_fields=None):
    post_url = f"{self.base_url}lists/{list_id}/members/{subscriber_hash}"
    post_body = {}
    if status is not None:
      post_body['status'] = status
    if merge_fields is not None:
      post_body['merge_fields'] = merge_fields
    if email:
      post_body['email_address'] = email
    result = put(post_url, self.headers, json.dumps(post_body))
    if not Utils.is_success(result['status_code']):
      if 'has signed up to a lot of lists very recently' in result['content']['detail']:
        return result
      else:
        raise Exception(f"Failed to update list member. Result: {result}")
    return result
