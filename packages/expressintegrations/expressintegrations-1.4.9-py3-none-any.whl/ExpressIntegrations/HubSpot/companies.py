from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS


def search_companies_by_property_value(property_name, property_value, property_names=None, after=None):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'EQ',
          'value': property_value
      }
  ]
  return search_companies(property_names, filters, after)


def search_companies_by_property_known(property_name, property_names=None, after=None):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'HAS_PROPERTY'
      }
  ]
  return search_companies(property_names, filters, after)


def search_companies_by_property_less_than(property_name, property_value, property_names=None, after=None):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'LT',
          'value': property_value
      }
  ]
  return search_companies(property_names, filters, after)


def search_companies_by_property_greater_than(property_name, property_value, property_names=None, after=None):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'GT',
          'value': property_value
      }
  ]
  return search_companies(property_names, filters, after)


def search_companies_by_property_values(property_name, property_values, property_names=None, after=None):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'IN',
          'values': property_values
      }
  ]
  return search_companies(property_names, filters, after)


def search_companies(property_names, filters, after=None):
  post_url = f"{BASE_URL}crm/v3/objects/companies/search"
  if after:
    post_url = f"{post_url}?after={after}"
  post_body = {
      'filterGroups': [
          {
              'filters': filters
          }
      ],
      'sorts': [],
      'limit': 100
  }
  if property_names:
    post_body['properties'] = property_names
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to search companies. Result: {result}")
  return result


def get_company(company_id, property_names=None, associations=None):
  post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}?archived=false"
  if property_names:
    post_url = f"{post_url}&properties={'%2C'.join(property_names)}"

  if associations:
    post_url = f"{post_url}&associations={'%2C'.join(associations)}"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve company. Result: {result}")
  return result


def create_company(properties):
  post_url = f"{BASE_URL}crm/v3/objects/companies"
  post_body = {
      'properties': properties
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create company. Result: {result}")
  return result


def update_company(company_id, properties):
  post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}?"
  post_body = {
      'properties': properties
  }
  result = patch(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update company. Result: {result}")
  return result
