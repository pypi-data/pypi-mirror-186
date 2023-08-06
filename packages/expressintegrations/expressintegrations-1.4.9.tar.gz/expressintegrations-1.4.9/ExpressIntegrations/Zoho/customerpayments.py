from ..HTTP.Requests import *
from .zoho import HEADERS
from .zoho import authenticate

BASE_URL = 'https://books.zoho.com/api/v3/customerpayments'


def create_customerpayment(customerpayment):
  authenticate()
  post_url = f"{BASE_URL}"
  result = post(post_url, HEADERS, json.dumps(customerpayment))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(post_url, HEADERS, json.dumps(customerpayment))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create customerpayment. Result: {result}")
  return result


def update_customerpayment(customerpayment_id, customerpayment):
  authenticate()
  post_url = f"{BASE_URL}/{customerpayment_id}"
  result = put(post_url, HEADERS, json.dumps(customerpayment))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = put(post_url, HEADERS, json.dumps(customerpayment))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update customerpayment. Result: {result}")
  return result


def get_customerpayment(customerpayment_id):
  authenticate()
  post_url = f"{BASE_URL}/{customerpayment_id}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve customerpayment. Result: {result}")
  return result


def search_customerpayments(customer_name=None,
                            reference_number=None,
                            date=None,
                            amount=None,
                            notes=None,
                            payment_mode=None,
                            due_date=None,
                            status=None,
                            customer_id=None,
                            filter_by=None,
                            search_text=None,
                            sort_column='date',
                            **kwargs):
  authenticate()
  # filter_by Allowed Values: Status.All, Status.Sent, Status.Draft, Status.OverDue, Status.Paid, Status.Void, Status.Unpaid, Status.PartiallyPaid, Status.Viewed and Date.PaymentExpectedDate
  # sort_column Allowed Values: customer_name, customerpayment_number, date, due_date, total, balance and created_time
  post_url = f"{BASE_URL}?sort_column={sort_column}"
  if customer_name is not None:
    post_url = f"{post_url}&customer_name={customer_name}"
  if reference_number is not None:
    post_url = f"{post_url}&reference_number={reference_number}"
  if date is not None:
    post_url = f"{post_url}&date={date}"
  if amount is not None:
    post_url = f"{post_url}&amount={amount}"
  if notes is not None:
    post_url = f"{post_url}&notes={notes}"
  if payment_mode is not None:
    post_url = f"{post_url}&payment_mode={payment_mode}"
  if due_date is not None:
    post_url = f"{post_url}&due_date={due_date}"
  if status is not None:
    post_url = f"{post_url}&status={status}"
  if customer_id is not None:
    post_url = f"{post_url}&customer_id={customer_id}"
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
    raise Exception(f"Failed to retrieve customerpayments. Result: {result}")
  return result
