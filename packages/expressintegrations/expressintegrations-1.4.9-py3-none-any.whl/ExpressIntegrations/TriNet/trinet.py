import base64

from ..HTTP.Requests import *
from ..Utils import Utils
from datetime import datetime

BASE_URL = 'https://api.trinet.com'


class trinet:
  headers = None
  expires_at = None
  access_token = None
  auth_refreshed = False
  account_identifier = None

  def __init__(
      self,
      account_identifier=None,
      access_token=None,
      expires_at=0,
      client_id=None,
      client_secret=None
  ):
    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    self.headers['Authorization'] = f"Bearer {access_token}"
    self.expires_at = expires_at
    self.access_token = access_token
    self.account_identifier = account_identifier
    self.base_url = f"{BASE_URL}/v1/company/{self.account_identifier}"
    self.auth_refreshed = False
    if client_id is None:
      raise Exception("Client ID must be provided")
    if client_secret is None:
      raise Exception("Client secret must be provided")

    if datetime.now().timestamp() > expires_at:
      self.authenticate(client_id, client_secret)
      self.auth_refreshed = True

  def authenticate(self, client_id, client_secret):
    user = f"{client_id}:{client_secret}"
    AUTH_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.b64encode(user.encode('UTF-8')).decode('UTF-8')}"
    }
    post_url = f"{BASE_URL}/oauth/accesstoken"
    auth_body = {
        'grant_type': 'client_credentials'
    }
    result = get(post_url, headers=AUTH_HEADERS, params=auth_body)
    auth_result = result['content']
    self.access_token = auth_result['access_token']
    self.headers['Authorization'] = f"Bearer {self.access_token}"
    self.expires_at = datetime.now().timestamp() + int(auth_result['expires_in'])

  def list_all_employees(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/employees"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get employees. Result: {result}")
    return result

  def get_company_details(self, params=None):
    post_url = f"{BASE_URL}/v1/manage-company/{self.account_identifier}/org-details"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get company details. Result: {result}")
    return result

  def list_supervisors(self):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/supervisors"
    result = get(post_url, headers=self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get supervisors. Result: {result}")
    return result

  def list_company_benefit_classes(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/benefit-classes"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get benefit-classes. Result: {result}")
    return result

  def list_company_benefits(self):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/benefits"
    result = get(post_url, headers=self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get benefits. Result: {result}")
    return result

  def list_company_savings_plans(self):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/savings-plans"
    result = get(post_url, headers=self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get savings-plans. Result: {result}")
    return result

  def list_company_changes(self, params=None):
    post_url = f"{BASE_URL}/v1/platform/company-changes"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get company-changes. Result: {result}")
    return result

  def list_employee_changes(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/employee-changes"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get employee-changes. Result: {result}")
    return result

  def list_departments(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/departments"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get departments. Result: {result}")
    return result

  def list_locations(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/locations"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get locations. Result: {result}")
    return result

  def list_job_codes(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/jobs"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get jobs. Result: {result}")
    return result

  def list_pay_codes(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/pay-codes"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get pay-codes. Result: {result}")
    return result

  def list_payroll_schedules(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/payroll-schedules"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get payroll-schedules. Result: {result}")
    return result

  def list_paygroups(self, params=None):
    post_url = f"{BASE_URL}/v1/company/{self.account_identifier}/paygroups"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get paygroups. Result: {result}")
    return result

  def get_employee_pay_info(self, employee_id, params=None):
    post_url = f"{BASE_URL}/v1/payroll/{self.account_identifier}/{employee_id}/pay-info"
    result = get(post_url, headers=self.headers, params=params)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get pay-info for {employee_id}. Result: {result}")
    return result

  def get_employee_retirement_plan_elections(self, employee_id):
    post_url = f"{BASE_URL}/v1/retirement-plan/{self.account_identifier}/{employee_id}/contributions"
    result = get(post_url, headers=self.headers)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to get retirement plan elections for {employee_id}. Result: {result}")
    return result
