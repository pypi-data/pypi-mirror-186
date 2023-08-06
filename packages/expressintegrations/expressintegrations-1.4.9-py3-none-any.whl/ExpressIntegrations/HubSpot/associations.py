from ..HTTP.Requests import *
from .hubspot import BASE_URL
from .hubspot import HEADERS


def get_associations(from_object_type, to_object_type, from_object_id):
  post_url = f"{BASE_URL}crm/v3/associations/{from_object_type}/{to_object_type}/batch/read"
  post_body = {
      'inputs': [
          {
              'id': from_object_id
          }
      ]
  }
  result = post(post_url, HEADERS, json.dumps(post_body))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve associations. Result: {result}")
  return result


def set_parent_company(company_id, parent_company_id):
  post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}/associations/company/{parent_company_id}/CHILD_TO_PARENT_COMPANY"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set parent company. Result: {result}")
  return result


def set_child_company(company_id, child_company_id):
  post_url = f"{BASE_URL}crm/v3/objects/companies/{company_id}/associations/company/{child_company_id}/PARENT_TO_CHILD_COMPANY"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set child company. Result: {result}")
  return result


def set_company_for_contact(contact_id, company_id):
  post_url = f"{BASE_URL}crm/v3/objects/contacts/{contact_id}/associations/company/{company_id}/CONTACT_TO_COMPANY"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set company for contact. Result: {result}")
  return result


def set_company_for_deal(deal_id, company_id):
  post_url = f"{BASE_URL}crm/v3/objects/deals/{deal_id}/associations/company/{company_id}/DEAL_TO_COMPANY"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set company for deal. Result: {result}")
  return result


def delete_company_from_deal(deal_id, company_id):
  post_url = f"{BASE_URL}crm/v3/objects/deals/{deal_id}/associations/company/{company_id}/DEAL_TO_COMPANY"
  result = delete(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to delete company from deal. Result: {result}")
  return result


def set_contact_for_deal(deal_id, contact_id):
  post_url = f"{BASE_URL}crm/v3/objects/deals/{deal_id}/associations/contact/{contact_id}/DEAL_TO_CONTACT"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set contact for deal. Result: {result}")
  return result


def set_deal_for_line_item(line_item_id, deal_id):
  post_url = f"{BASE_URL}crm/v3/objects/line_items/{line_item_id}/associations/deals/{deal_id}/LINE_ITEM_TO_DEAL"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set deal for line item. Result: {result}")
  return result


def set_contact_for_meeting(meeting_id, contact_id):
  post_url = f"{BASE_URL}crm/v3/objects/meetings/{meeting_id}/associations/contacts/{contact_id}/MEETING_EVENT_TO_CONTACT"
  result = put(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to set contact for meeting. Result: {result}")
  return result
