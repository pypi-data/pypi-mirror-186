from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS


def get_owner(owner_id):
  post_url = f"{BASE_URL}crm/v3/owners/{owner_id}"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve owner. Result: {result}")
  return result


def search_owners(email=None, limit=100, after=None):
  post_url = f"{BASE_URL}crm/v3/owners?limit={limit}"
  if email is not None:
    post_url = f"{post_url}&email={email}"
  if after is not None:
    post_url = f"{post_url}&after={after}"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to search owners. Result: {result}")
  return result
