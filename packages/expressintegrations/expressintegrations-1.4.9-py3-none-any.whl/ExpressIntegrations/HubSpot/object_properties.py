from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS


def get_properties(object_type):
  post_url = f"{BASE_URL}crm/v3/properties/{object_type}?archived=false"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to get properties. Result: {result}")
  return result


def get_property(object_type, property_name):
  post_url = f"{BASE_URL}crm/v3/properties/{object_type}/{property_name}?archived=false"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to get property. Result: {result}")
  return result


def update_property(object_type, property_name, data):
  post_url = f"{BASE_URL}crm/v3/properties/{object_type}/{property_name}"
  acceptable_keys = [
      'groupName',
      'hidden',
      'displayOrder',
      'options',
      'label',
      'type',
      'fieldType',
      'formField'
  ]
  data = {k: v for k, v in data.items() if k in acceptable_keys}
  result = patch(post_url, HEADERS, payload=json.dumps(data))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update property. Result: {result}")
  return result
