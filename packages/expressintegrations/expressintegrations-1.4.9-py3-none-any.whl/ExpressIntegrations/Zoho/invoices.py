from ..HTTP.Requests import *
from .zoho import HEADERS
from .zoho import authenticate

BASE_URL = 'https://books.zoho.com/api/v3/invoices'


def create_invoice(invoice):
  authenticate()
  post_url = f"{BASE_URL}"
  result = post(post_url, HEADERS, json.dumps(invoice))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(post_url, HEADERS, json.dumps(invoice))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create invoice. Result: {result}")
  return result


def update_invoice(invoice_id, invoice):
  authenticate()
  post_url = f"{BASE_URL}/{invoice_id}"
  result = put(post_url, HEADERS, json.dumps(invoice))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = put(post_url, HEADERS, json.dumps(invoice))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update invoice. Result: {result}")
  return result


def get_invoice(invoice_id):
  authenticate()
  post_url = f"{BASE_URL}/{invoice_id}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve invoice. Result: {result}")
  return result


def search_invoices(invoice_number=None,
                    item_name=None,
                    item_id=None,
                    item_description=None,
                    reference_number=None,
                    customer_name=None,
                    recurring_invoice_id=None,
                    email=None,
                    total=None,
                    balance=None,
                    date=None,
                    due_date=None,
                    status=None,
                    customer_id=None,
                    filter_by=None,
                    search_text=None,
                    sort_column='created_time',
                    **kwargs):
  authenticate()
  # filter_by Allowed Values: Status.All, Status.Sent, Status.Draft, Status.OverDue, Status.Paid, Status.Void, Status.Unpaid, Status.PartiallyPaid, Status.Viewed and Date.PaymentExpectedDate
  # sort_column Allowed Values: customer_name, invoice_number, date, due_date, total, balance and created_time
  post_url = f"{BASE_URL}?sort_column={sort_column}"
  if invoice_number is not None:
    post_url = f"{post_url}&invoice_number={invoice_number}"
  if item_name is not None:
    post_url = f"{post_url}&item_name={item_name}"
  if item_id is not None:
    post_url = f"{post_url}&item_id={item_id}"
  if item_description is not None:
    post_url = f"{post_url}&item_description={item_description}"
  if reference_number is not None:
    post_url = f"{post_url}&reference_number={reference_number}"
  if customer_name is not None:
    post_url = f"{post_url}&customer_name={customer_name}"
  if recurring_invoice_id is not None:
    post_url = f"{post_url}&recurring_invoice_id={recurring_invoice_id}"
  if email is not None:
    post_url = f"{post_url}&email={email}"
  if total is not None:
    post_url = f"{post_url}&total={total}"
  if balance is not None:
    post_url = f"{post_url}&balance={balance}"
  if date is not None:
    post_url = f"{post_url}&date={date}"
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
    raise Exception(f"Failed to retrieve invoices. Result: {result}")
  return result
