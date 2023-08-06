from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS
from . import object_properties


def search_contacts_by_property_value(property_name, property_value, property_names=None, after=None, sorts=[]):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'EQ',
          'value': property_value
      }
  ]
  return search_contacts(property_names, filters, after, sorts)


def search_contacts_by_property_known(property_name, property_names, after=None, sorts=[]):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'HAS_PROPERTY'
      }
  ]
  return search_contacts(property_names, filters, after, sorts)


def search_contacts_by_property_less_than(property_name, property_value, property_names, after=None, sorts=[]):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'LT',
          'value': property_value
      }
  ]
  return search_contacts(property_names, filters, after, sorts)


def search_contacts_by_property_greater_than(property_name, property_value, property_names, after=None, sorts=[]):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'GT',
          'value': property_value
      }
  ]
  return search_contacts(property_names, filters, after, sorts)


def search_contacts_by_property_values(property_name, property_values, property_names, after=None, sorts=[]):
  filters = [
      {
          'propertyName': property_name,
          'operator': 'IN',
          'values': property_values
      }
  ]
  return search_contacts(property_names, filters, after, sorts)


def search_contacts(property_names, filters, after=None, sorts=[]):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/search"
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
    raise Exception(f"Failed to search contacts. Result: {result}")
  return result


def read_contacts_batch(properties, inputs, id_property=None):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/batch/read"
  post_body = {
      'properties': properties,
      'inputs': inputs
  }
  if id_property is not None:
    post_body['idProperty'] = id_property
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to read contacts. Result: {result}")
  return result


def get_contact(contact_id, property_names=None, associations=None):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}?archived=false"
  if property_names:
    post_url = f"{post_url}&properties={'%2C'.join(property_names)}"

  if associations:
    post_url = f"{post_url}&associations={'%2C'.join(associations)}"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve contact. Result: {result}")
  return result


def create_contact(properties):
  post_url = f"{BASE_URL}crm/v3/objects/contacts"
  post_body = {
      'properties': properties
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create contact. Result: {result}")
  return result


def create_contacts_batch(contacts):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/batch/create"
  post_body = {
      'inputs': contacts
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create contacts. Result: {result}")
  return result


def update_contact(contact_id, properties):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}?"
  post_body = {
      'properties': properties
  }
  result = patch(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update contact. Result: {result}")
  return result


def update_contacts_batch(contacts):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/batch/update"
  post_body = {
      'inputs': contacts
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update contacts. Result: {result}")
  return result


def delete_contact(contact_id):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}"
  result = delete(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to delete contact. Result: {result}")
  return result


def unsubscribe_from_all(contact_email):
  post_url = f"{BASE_URL}email/public/v1/subscriptions/{contact_email}"
  post_body = {
      'unsubscribeFromAll': True
  }
  result = put(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to unsubscribe contact. Result: {result}")
  return result


def get_contact_properties():
  return object_properties.get_properties('contacts')


def get_contact_property(property_name):
  return object_properties.get_property('contacts', property_name)


def update_contact_property(property_name, data):
  return object_properties.update_property('contacts', property_name, data)
