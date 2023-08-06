import time
from datetime import datetime, timezone
import calendar

from collections import defaultdict

epoch = datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)

def access_secret_version(project_id, secret_id, version_id):
  """
  Access the payload for the given secret version if one exists. The version
  can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
  """

  # Import the Secret Manager client library.
  from google.cloud import secretmanager

  # Create the Secret Manager client.
  client = secretmanager.SecretManagerServiceClient()

  # Build the resource name of the secret version.
  name = client.secret_version_path(project_id, secret_id, version_id)

  # Access the secret version.
  response = client.access_secret_version(name)

  # Print the secret payload.
  #
  # WARNING: Do not print the secret in a production environment - this
  # snippet is showing how to access the secret material.
  payload = response.payload.data.decode('UTF-8')
  return payload

def format_date_time(epoch_ms):
  if not epoch_ms:
    return None
  return datetime.utcfromtimestamp(int(epoch_ms)//1000).replace(microsecond=int(epoch_ms)%1000*1000)

def date_from_epoch_ms(epoch_ms):
  date_time = format_date_time(epoch_ms)
  if not date_time:
    return None
  return date_time.date()

def closest_date_next_month(year, month, day):
    month = month + 1
    if month == 13:
      month = 1
      year = year + 1

    condition = True
    while condition:
      try:
        return datetime(year, month, day)
      except ValueError:
        day = day-1
      condition = day > 26

    raise Exception('Problem getting date next month')

def pass_job(job, start_time, success, event, error, results, job_history=None):
  if job_history:
    job_history.update(
      start_time=start_time,
      end_time=datetime.now(),
      success=success,
      input=event,
      error=error,
      results=results
    )
  else:
    job_history = app_tables.job_history.add_row(
      job=job,
      start_time=start_time,
      end_time=datetime.now(),
      success=success,
      input=event,
      error=error,
      results=results
    )
  return job_history

def fail_job(job, job_name, user_email, start_time, event, error, results, stack_trace, job_history=None):
  if job_history:
    job_history.update(
      start_time=start_time,
      end_time=datetime.now(),
      success=False,
      input=event,
      error=error,
      results=results
    )
  else:
    job_history = app_tables.job_history.add_row(
      job=job,
      start_time=start_time,
      end_time=datetime.now(),
      success=False,
      input=event,
      error=error,
      results=results
    )
  anvil.server.call('send_admin_error_email', job_name, user_email, start_time, event, error, stack_trace)
  return job_history
    
def start_admin_job(job_history):
  job_start_time = now()
  job_history.update(last_job_start_time=format_date_time(job_start_time),status="running...")
  return job_start_time
  
def pass_admin_job(job_history, job_start_time, results):
  job_end_time = now()
  job_history.update(
    last_job_run_results=results,
    last_job_end_time=format_date_time(job_end_time),
    status="completed successfully",
    last_successful_run_time=format_date_time(job_end_time),
    last_job_duration=round((job_end_time - job_start_time)/1000, 3)
  )

def fail_admin_job(job_history, job_start_time, results, message):
  job_end_time = now()
  job_history.update(
    last_job_run_results=results,
    last_job_end_time=format_date_time(job_end_time),
    status=f"failed: {message}",
    last_job_duration=round((job_end_time - job_start_time)/1000, 3)
  )

def now():
  return round(time.time() * 1000)

def getEpochMillis(dt):
  return (dt - epoch).total_seconds() * 1000

def validateDateAndReturnEpochTimeInMillis(date):
  date = str(date).replace("-", "/").replace(".", "/")
  yyyy, mm, dd = date.split('/')
  dd = int(dd.lstrip("0"))
  mm = int(mm.lstrip("0"))
  yyyy = int(yyyy)
  if mm in [1, 3, 5, 7, 8, 10, 12]:
      maxDay = 31
  elif mm in [4, 6, 9, 11]:
      maxDay = 30
  elif yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0:
      maxDay = 29
  else:
      maxDay = 28

  if mm < 1 or mm > 12:
     raise Exception("Please specify a valid month.")
  elif dd < 1 or dd > maxDay:
    raise Exception("Please specify a valid day.")
  elif len(f"{yyyy}") != 4:
    raise Exception("Please specify a valid 4-digit year.")
  else:
    dateTime = f"{date} 00:00:00"
    epoch = int(time.mktime(time.strptime(dateTime, "%Y/%m/%d %H:%M:%S"))) * 1000

  return epoch

def partition(seq, key):
  d = {}
  for x in seq:
    d[key(x)] = []
  return d

def makehash():
  return defaultdict(makehash)

def get_filtered_dict(search_term, dictionary):
    return {k: v for k, v in dictionary.items() if any(search_term in str(x).lower() for x in v.values())}

def is_success(status_code):
  return str(status_code).startswith('2')

def is_not_found(status_code):
  return str(status_code) == '404'

def is_retryable(status_code):
  return str(status_code) in ['502', '429'] or not status_code

def validate_response(response, error_message, success_message=None):
  if not is_success(response['status_code']):
    response['error_message'] = '%s %s:%s' % (error_message, response['status_code'], response['content'])
  elif success_message != None:
    response['success_message'] = success_message
  return response

def remove_keys_from_dict(d, keys):
  return {k: v for k, v in d.items() if k not in keys}
      
def remove_keys_from_dict_except(d, keys):
  return {k: v for k, v in d.items() if k in keys}
  
def apply_func_to_items(iterable, func):
  return map(lambda x : func(x), iterable)