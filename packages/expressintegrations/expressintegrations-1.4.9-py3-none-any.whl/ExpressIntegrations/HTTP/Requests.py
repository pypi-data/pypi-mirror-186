import json
import requests
import time

URL = 'url'
METHOD = 'method'
HEADERS = 'headers'
DATA = 'data'
STATUS_CODE = 'status_code'
CONTENT = 'content'


def is_success(status_code):
  return str(status_code).startswith('2')


def is_not_found(status_code):
  return str(status_code) == '404'


def is_retryable(status_code):
  return str(status_code) in ['502', '429'] or not status_code


def is_unauthorized(status_code):
  return str(status_code) in ['401', '403']


def is_json(value):
  if not value:
    return False
  try:
    json.loads(value)
  except ValueError:
    return False
  return True


def request(method, url, **kwargs):
  result = getattr(requests, method.lower())(url, **kwargs)
  wait = 1
  while is_retryable(result.status_code):
    time.sleep(wait)
    wait = wait * 2 if wait < 10 else 10
    result = getattr(requests, method.lower())(url, **kwargs)
  content = None
  if result.text and is_json(result.text):
    content = json.loads(result.text)
  return {
      URL: url,
      HEADERS: kwargs.get(HEADERS),
      METHOD: method,
      DATA: kwargs.get(DATA),
      STATUS_CODE: result.status_code,
      CONTENT: content
  }


def post(url, **kwargs):
  return request('post', url, **kwargs)


def patch(url, **kwargs):
  return request('patch', url, **kwargs)


def get(url, **kwargs):
  return request('get', url, **kwargs)


def put(url, **kwargs):
  return request('put', url, **kwargs)


def delete(url, **kwargs):
  return request('delete', url, **kwargs)
