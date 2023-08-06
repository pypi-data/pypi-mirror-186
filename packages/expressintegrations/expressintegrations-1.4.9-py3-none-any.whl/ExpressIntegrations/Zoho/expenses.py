from ..HTTP.Requests import *
from .zoho import HEADERS
from .zoho import authenticate

BASE_URL = 'https://books.zoho.com/api/v3/expenses'


def create_expense(expense):
  authenticate()
  post_url = f"{BASE_URL}"
  result = post(post_url, HEADERS, json.dumps(expense))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = post(post_url, HEADERS, json.dumps(expense))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create expense. Result: {result}")
  return result


def update_expense(expense_id, expense):
  authenticate()
  post_url = f"{BASE_URL}/{expense_id}"
  result = put(post_url, HEADERS, json.dumps(expense))
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = put(post_url, HEADERS, json.dumps(expense))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update expense. Result: {result}")
  return result


def get_expense(expense_id):
  authenticate()
  post_url = f"{BASE_URL}/{expense_id}"
  result = get(post_url, HEADERS)
  if Utils.is_unauthorized(result['status_code']):
    authenticate(force=True)
    result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve expense. Result: {result}")
  return result


def search_expenses(description=None,
                    reference_number=None,
                    date=None,
                    status=None,
                    amount=None,
                    account_name=None,
                    customer_name=None,
                    vendor_name=None,
                    customer_id=None,
                    vendor_id=None,
                    recurring_expense_id=None,
                    paid_through_account_id=None,
                    search_text=None,
                    filter_by=None,
                    sort_column='created_time',
                    **kwargs):
  authenticate()
  post_url = f"{BASE_URL}?sort_column={sort_column}"
  if description is not None:
    post_url = f"{post_url}&description={description}"
  if reference_number is not None:
    post_url = f"{post_url}&reference_number={reference_number}"
  if date is not None:
    post_url = f"{post_url}&date={date}"
  if status is not None:
    post_url = f"{post_url}&status={status}"
  if amount is not None:
    post_url = f"{post_url}&amount={amount}"
  if account_name is not None:
    post_url = f"{post_url}&account_name={account_name}"
  if customer_name is not None:
    post_url = f"{post_url}&customer_name={customer_name}"
  if vendor_name is not None:
    post_url = f"{post_url}&vendor_name={vendor_name}"
  if customer_id is not None:
    post_url = f"{post_url}&customer_id={customer_id}"
  if vendor_id is not None:
    post_url = f"{post_url}&vendor_id={vendor_id}"
  if recurring_expense_id is not None:
    post_url = f"{post_url}&recurring_expense_id={recurring_expense_id}"
  if paid_through_account_id is not None:
    post_url = f"{post_url}&paid_through_account_id={paid_through_account_id}"
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
    raise Exception(f"Failed to retrieve expenses. Result: {result}")
  return result
