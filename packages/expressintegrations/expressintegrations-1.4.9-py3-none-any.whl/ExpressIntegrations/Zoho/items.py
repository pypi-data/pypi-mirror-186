from ..HTTP.Requests import *
from .zoho import HEADERS
from .zoho import authenticate

BASE_URL = 'https://books.zoho.com/api/v3/items'


def create_item(item):
  authenticate()
  post_url = f"{BASE_URL}"
  result = post(post_url, HEADERS, json.dumps(item))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(post_url, HEADERS, json.dumps(item))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create item. Result: {result}")
  return result


def update_item(item_id, item):
  authenticate()
  post_url = f"{BASE_URL}/{item_id}"
  result = put(post_url, HEADERS, json.dumps(item))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = put(post_url, HEADERS, json.dumps(item))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update item. Result: {result}")
  return result


def get_item(item_id):
  authenticate()
  post_url = f"{BASE_URL}/{item_id}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve item. Result: {result}")
  return result


def search_items(name=None,
                 description=None,
                 rate=None,
                 tax_id=None,
                 filter_by=None,
                 search_text=None,
                 sort_column='created_time',
                 **kwargs):
  authenticate()
  # filter_by Allowed Values: Status.All, Status.Active and Status.Inactive
  # sort_column Allowed Values: name, rate and tax_name
  post_url = f"{BASE_URL}?sort_column={sort_column}"
  if name is not None:
    post_url = f"{post_url}&name={name}"
  if description is not None:
    post_url = f"{post_url}&description={description}"
  if rate is not None:
    post_url = f"{post_url}&rate={rate}"
  if tax_id is not None:
    post_url = f"{post_url}&tax_id={tax_id}"
  if filter_by is not None:
    post_url = f"{post_url}&filter_by={filter_by}"
  if search_text is not None:
    post_url = f"{post_url}&search_text={search_text}"
  for name, value in kwargs.items():
    post_url = f"{post_url}&{name}={value}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve items. Result: {result}")
  return result
