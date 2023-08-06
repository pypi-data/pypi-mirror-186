from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS
from . import object_properties


def search_engagements_by_property_value(engagement_type, property_name, property_value, property_names=None, after=None, sorts=[]):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'EQ',
          'value': property_value
      }
  ]
  return search_engagements(engagement_type, property_names, filters, after, sorts)


def search_engagements(engagement_type, property_names, filters, after=None, sorts=[]):
  post_url = f"{BASE_URL}crm/v3/objects/{engagement_type}/search"
  if after:
    post_url = f"{post_url}?after={after}"
  post_body = {
      'filterGroups': [
          {
              'filters': filters
          }
      ],
      'sorts': sorts,
      'properties': property_names,
      'limit': 100
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to search {engagement_type}. Result: {result}")
  return result


def create_engagement(engagement_type, properties):
  post_url = f"{BASE_URL}crm/v3/objects/{engagement_type}"
  post_body = {
      'properties': properties
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create {engagement_type}. Result: {result}")
  return result


def update_engagement(engagement_id, engagement_type, properties):
  post_url = f"{BASE_URL}crm/v3/objects/{engagement_type}/{engagement_id}?"
  post_body = {
      'properties': properties
  }
  result = patch(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update engagement. Result: {result}")
  return result


def get_engagement_properties():
  return object_properties.get_properties('engagements')


def get_engagement_property(property_name):
  return object_properties.get_property('engagements', property_name)


def update_engagement_property(property_name, data):
  return object_properties.update_property('engagements', property_name, data)
