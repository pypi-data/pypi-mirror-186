from ..HTTP.Requests import *
from .zoho import HEADERS
from .zoho import authenticate

BASE_URL = 'https://books.zoho.com/api/v3'


def create_user(user):
  authenticate()
  post_url = f"{BASE_URL}/users"
  result = post(post_url, HEADERS, json.dumps(user))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(post_url, HEADERS, json.dumps(user))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create user. Result: {result}")
  return result


def update_user(user_id, user):
  authenticate()
  post_url = f"{BASE_URL}/users/{user_id}"
  result = put(post_url, HEADERS, json.dumps(user))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = put(post_url, HEADERS, json.dumps(user))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update user. Result: {result}")
  return result


def get_user(user_id):
  authenticate()
  post_url = f"{BASE_URL}/users/{user_id}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve user. Result: {result}")
  return result


def search_users(filter_by=None, sort_column='email', **kwargs):
  authenticate()
  # sort_column Allowed Values: name, email, user_role and status
  post_url = f"{BASE_URL}/users?sort_column={sort_column}"
  if filter_by is not None:
    post_url = f"{post_url}&filter_by={filter_by}"
  for name, value in kwargs.items():
    post_url = f"{post_url}&{name}={value}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve users. Result: {result}")
  return result


def get_salesperson(salesperson_id):
  authenticate()
  SALESPERSON_ID = 'salesperson_id'
  CONTENT = 'content'
  DATA = 'data'
  result = search_salespersons()
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = search_salespersons()
  salespersons = {item[SALESPERSON_ID]: item for item in result[CONTENT][DATA]}
  return salespersons.get(salesperson_id)


def search_salespersons():
  authenticate()
  post_url = f"{BASE_URL}/salespersons"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to search salespersons. Result: {result}")
  return result


def create_salesperson(name, email):
  authenticate()
  post_url = f"{BASE_URL}/salespersons"
  post_body = {
      'salesperson_name': name,
      'salesperson_email': email
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create salesperson. Result: {result}")
  return result
