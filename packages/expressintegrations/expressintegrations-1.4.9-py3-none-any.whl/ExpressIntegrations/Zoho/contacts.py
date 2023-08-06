from ..HTTP.Requests import *
from .zoho import HEADERS
from .zoho import authenticate
from ..Utils import Utils

BASE_URL = 'https://books.zoho.com/api/v3/contacts'


def create_contact(contact):
  authenticate()
  result = post(BASE_URL, HEADERS, json.dumps(contact))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(BASE_URL, HEADERS, json.dumps(contact))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create contact. Result: {result}")
  return result


def update_contact(contact_id, contact):
  authenticate()
  post_url = f"{BASE_URL}/{contact_id}"
  result = put(post_url, HEADERS, json.dumps(contact))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = put(post_url, HEADERS, json.dumps(contact))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update contact. Result: {result}")
  return result


def get_contact(contact_id):
  authenticate()
  post_url = f"{BASE_URL}/{contact_id}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve contact. Result: {result}")
  return result


def search_contacts(contact_name=None,
                    company_name=None,
                    first_name=None,
                    last_name=None,
                    address=None,
                    email=None,
                    phone=None,
                    filter_by=None,
                    search_text=None,
                    sort_column='created_time',
                    **kwargs):
  authenticate()
  # filter_by Allowed Values: Status.All, Status.Active, Status.Inactive, Status.Duplicate and Status.Crm
  # sort_column Allowed Values: contact_name, first_name, last_name, email, outstanding_receivable_amount, created_time and last_modified_time
  post_url = f"{BASE_URL}?sort_column={sort_column}"
  if contact_name is not None:
    post_url = f"{post_url}&contact_name={contact_name}"
  if company_name is not None:
    post_url = f"{post_url}&company_name={company_name}"
  if first_name is not None:
    post_url = f"{post_url}&first_name={first_name}"
  if last_name is not None:
    post_url = f"{post_url}&last_name={last_name}"
  if address is not None:
    post_url = f"{post_url}&address={address}"
  if email is not None:
    post_url = f"{post_url}&email={email}"
  if phone is not None:
    post_url = f"{post_url}&phone={phone}"
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
    raise Exception(f"Failed to retrieve contacts. Result: {result}")
  return result
