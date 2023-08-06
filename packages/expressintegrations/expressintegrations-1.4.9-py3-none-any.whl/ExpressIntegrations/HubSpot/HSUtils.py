import requests
import json
from datetime import date, timedelta
from ..HTTP.Requests import *
from ..Utils import Utils

# Generic Variables
auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
BASE_URL = "https://api.hubapi.com/"

DEFAULT_BATCH_SIZE = 500

class HSUtils:
  def __init__(self, project_id, refresh_token):
    self.headers={"Content-Type": "application/json","Accept": "application/json"}
    self.refresh_token = refresh_token
    post_url = f"{BASE_URL}oauth/v1/token"
    auth_body = {
      'grant_type': 'refresh_token',
      'client_id': Utils.access_secret_version(project_id, 'hs_client_id', 'latest'),
      'client_secret': Utils.access_secret_version(project_id, 'hs_client_secret', 'latest'),
      'refresh_token': self.refresh_token
    }
    result = post(post_url, auth_headers, auth_body)
    auth_result = result['content']
    self.headers['Authorization'] = f"Bearer {auth_result['access_token']}"

  # Contains utilities for interacting with the HubSpot API
  def get_token_details(self):
    post_url = f"{BASE_URL}oauth/v1/refresh-tokens/{self.refresh_token}"
    return get(post_url, self.headers)
  
  def revoke_token(self):
    headers = {
      'Content-type': 'application/x-www-form-urlencoded'
    }
    post_url = f"{BASE_URL}oauth/v1/refresh-tokens/{self.refresh_token}"
    return delete(post_url, headers)
  
  def create_contact(self, properties):
    post_url = f"{BASE_URL}contacts/v1/contact/"
    post_body = {
      'properties': self.format_properties(properties)
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def create_or_update_contact(self, email, properties):
    if not email:
      return self.create_contact(properties)
    post_url = f"{BASE_URL}contacts/v1/contact/createOrUpdate/email/{email}"
    post_body = {
      'properties': self.format_properties(properties)
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def get_all_contacts_paged(self, property_names, vid_offset=""):
    post_url = f"{BASE_URL}contacts/v1/lists/all/contacts/all?count=100&vidOffset={vid_offset}"
    for property_name in property_names:
      post_url = f"{post_url}&property={property_name}"
    result = get(post_url, self.headers)
    return result
  
  def get_all_contacts(self, property_names):
    contacts = []
    contact_result = self.get_all_contacts_paged(property_names)
    contacts_paged = contact_result['content']
    contacts += contacts_paged['contacts']
    
    while contacts_paged['has-more']:
      contact_result = self.get_all_contacts_paged(property_names, contacts_paged['vid-offset'])
      contacts_paged = contact_result['content']
      contacts += contacts_paged['contacts']
    
    return contacts
  
  def create_deal(self, associated_vids, properties):
    post_url = f"{BASE_URL}deals/v1/deal"
    post_body = {
      'associations': {
        'associatedVids': associated_vids
      },
      'properties': self.format_deal_properties(properties)
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def get_contact_properties(self):
    post_url = f"{BASE_URL}properties/v1/contacts/properties"
    result = get(post_url, self.headers)
    return result
  
  def get_deal_property(self, name):
    post_url = f"{BASE_URL}properties/v1/deals/properties/named/{name}"
    result = get(post_url, self.headers)
    return result
  
  def get_deal_properties(self):
    post_url = f"{BASE_URL}properties/v1/deals/properties"
    result = get(post_url, self.headers)
    return result
  
  def get_line_items(self, line_item_ids, properties):
    post_url = f"{BASE_URL}crm-objects/v1/objects/line_items/batch-read?"
    if len(properties) > 0:
      post_url = f"{post_url}properties={'&properties='.join(properties)}"
    post_body = {
      'ids': line_item_ids
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def get_products(self, product_ids):
    post_url = f"{BASE_URL}crm-objects/v1/objects/products/batch-read"
    post_body = {
      'ids': product_ids
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def get_associations(self, from_object_type, to_object_type, from_object_id):
    post_url = f"{BASE_URL}crm/v3/associations/{from_object_type}/{to_object_type}/batch/read"
    post_body = {
      'inputs': [
        {
          'id': from_object_id
        }
      ]
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def search_contacts_by_property_value(self, property_name, property_value, property_names, after=None):
    filters = [
      {
        'propertyName': property_name,
        'operator': 'EQ',
        'value': property_value
      }
    ]
    return self.search_contacts(property_names, filters, after)

  def search_contacts_by_property_known(self, property_name, property_names, after=None):
    filters = [
      {
        'propertyName': property_name,
        'operator': 'HAS_PROPERTY'
      }
    ]
    return self.search_contacts(property_names, filters, after)

  def search_contacts_by_property_less_than(self, property_name, property_value, property_names, after=None):
    filters = [
      {
        'propertyName': property_name,
        'operator': 'LT',
        'value': property_value
      }
    ]
    return self.search_contacts(property_names, filters, after)

  def search_contacts_by_property_greater_than(self, property_name, property_value, property_names, after=None):
    filters = [
      {
        'propertyName': property_name,
        'operator': 'GT',
        'value': property_value
      }
    ]
    return self.search_contacts(property_names, filters, after)

  def search_contacts_by_property_values(self, property_name, property_values, property_names, after=None):
    filters = [
      {
        'propertyName': property_name,
        'operator': 'IN',
        'values': property_values
      }
    ]
    return self.search_contacts(property_names, filters, after)

  def search_contacts(self, property_names, filters, after=None):
    post_url = f"{BASE_URL}crm/v3/objects/contacts/search"
    if after:
      post_url = f"{post_url}?after={after}"
    post_body = {
      'filterGroups': [
        {
          'filters': filters
        }
      ],
      'sorts': [],
      'properties': property_names,
      'limit': 100
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result
  
  def get_contact(self, contact_id, property_names=None, associations=None):
    post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}?archived=false"
    if property_names:
      post_url = f"{post_url}&properties={'%2C'.join(property_names)}"
      
    if associations:
      post_url = f"{post_url}&associations={'%2C'.join(associations)}"
    result = get(post_url, self.headers)
    return result
  
  def update_contact(self, contact_id, properties):
    post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}?"
    post_body = {
      'properties': properties
    }
    result = patch(post_url, self.headers, json.dumps(post_body))
    return result
  
  def get_company(self, company_id, property_names=None, associations=None):
    post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}?archived=false"
    if property_names:
      post_url = f"{post_url}&properties={'%2C'.join(property_names)}"
      
    if associations:
      post_url = f"{post_url}&associations={'%2C'.join(associations)}"
    result = get(post_url, self.headers)
    return result

  def create_company(self, properties):
    post_url = f"{BASE_URL}crm/v3/objects/companies"
    post_body = {
      'properties': properties
    }
    result = post(post_url, self.headers, json.dumps(post_body))
    return result

  def update_company(self, company_id, properties):
    post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}?"
    post_body = {
      'properties': properties
    }
    result = patch(post_url, self.headers, json.dumps(post_body))
    return result

  def set_parent_company(self, company_id, parent_company_id):
    post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}/associations/company/{parent_company_id}/CHILD_TO_PARENT_COMPANY"
    result = put(post_url, self.headers)
    return result

  def set_child_company(self, company_id, child_company_id):
    post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}/associations/company/{child_company_id}/PARENT_TO_CHILD_COMPANY"
    result = put(post_url, self.headers)
    return result

  def set_company_for_contact(self, contact_id, company_id):
    post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}/associations/company/{company_id}/CONTACT_TO_COMPANY"
    result = put(post_url, self.headers)
    return result
  
  def get_quote(self, quote_id, property_names=None, associations=None):
    post_url = f"{BASE_URL}crm/v3/objects/quotes/{quote_id}?archived=false&hapikey=64e33cbd-e2ef-4534-8c7f-82e023e113e4"
    temp_headers = dict(self.headers)
    del temp_headers['Authorization']
    if property_names:
      post_url = f"{post_url}&properties={'%2C'.join(property_names)}"
      
    if associations:
      post_url = f"{post_url}&associations={'%2C'.join(associations)}"
    result = get(post_url, temp_headers)
    return result
  
  def get_deal(self, deal_id, property_names=None, associations=None):
    post_url = f"{BASE_URL}crm/v3/objects/deals/{deal_id}?archived=false"
    if property_names:
      post_url = f"{post_url}&properties={'%2C'.join(property_names)}"
      
    if associations:
      post_url = f"{post_url}&associations={'%2C'.join(associations)}"
    result = get(post_url, self.headers)
    return result
  
  def format_properties(self, properties):
    return [{"property": k, "value": v} for k, v in properties.items()]
  
  def format_deal_properties(self, properties):
    return [{"name": k, "value": v} for k, v in properties.items()]