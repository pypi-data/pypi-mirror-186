import requests
import json
import time
from .. import Utils

URL = 'url'
HEADERS = 'headers'
PAYLOAD = 'payload'
STATUS_CODE = 'status_code'
CONTENT = 'content'

def response_is_retryable(result):
  return Utils.is_retryable(result[STATUS_CODE])

@anvil.server.callable
def post(url, headers, payload=None, auth=None):
  result = requests.post(url, data=payload, headers=headers, auth=auth)
  wait = 1
  while Utils.is_retryable(result.status_code):
    time.sleep(wait)
    wait = wait * 2 if wait < 10 else 10
    result = requests.post(url, data=payload, headers=headers, auth=auth)
  content = None
  if result.text:
    content = json.loads(result.text)
  return {
    URL: url,
    HEADERS: headers,
    PAYLOAD: payload,
    STATUS_CODE: result.status_code,
    CONTENT: content
  }

@anvil.server.callable
def patch(url, headers, payload=None, auth=None):
  result = requests.patch(url, data=payload, headers=headers, auth=auth)
  wait = 1
  while Utils.is_retryable(result.status_code):
    time.sleep(wait)
    wait = wait * 2 if wait < 10 else 10
    result = requests.patch(url, data=payload, headers=headers, auth=auth)
  content = None
  if result.text:
    content = json.loads(result.text)
  return {
    URL: url,
    HEADERS: headers,
    PAYLOAD: payload,
    STATUS_CODE: result.status_code,
    CONTENT: content
  }

@anvil.server.callable
def get(url, headers, auth=None):
  result = requests.get(url, headers=headers, auth=auth)
  wait = 1
  while Utils.is_retryable(result.status_code):
    print(f"retrying. last result: {result}")
    time.sleep(wait)
    wait = wait * 2 if wait < 10 else 10
    result = requests.get(url, headers=headers, auth=auth)
  content = None
  if result.text:
    content = json.loads(result.text)
  return {
    URL: url,
    HEADERS: headers,
    STATUS_CODE: result.status_code,
    CONTENT: content
  }

@anvil.server.callable
def put(url, headers, payload=None, auth=None):
  result = requests.put(url, data=payload, headers=headers, auth=auth)
  wait = 1
  while Utils.is_retryable(result.status_code):
    time.sleep(wait)
    wait = wait * 2 if wait < 10 else 10
    result = requests.put(url, data=payload, headers=headers, auth=auth)
  content = None
  if result.text:
    content = json.loads(result.text)
  return {
    URL: url,
    HEADERS: headers,
    PAYLOAD: payload,
    STATUS_CODE: result.status_code,
    CONTENT: content
  }

@anvil.server.callable
def delete(url, headers, auth=None):
  result = requests.delete(url, headers=headers, auth=auth)
  wait = 1
  while Utils.is_retryable(result.status_code):
    time.sleep(wait)
    wait = wait * 2 if wait < 10 else 10
    result = requests.delete(url, headers=headers, auth=auth)
  content = None
  if result.text:
    content = json.loads(result.text)
  return {
    URL: url,
    HEADERS: headers,
    STATUS_CODE: result.status_code,
    CONTENT: content
  }