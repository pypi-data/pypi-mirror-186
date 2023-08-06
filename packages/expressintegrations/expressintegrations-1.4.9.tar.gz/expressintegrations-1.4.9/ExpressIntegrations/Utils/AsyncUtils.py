from __future__ import print_function

import datetime


def create_task(project, location, queue, relative_handler_uri, payload=None, in_seconds=None):
  # [START cloud_tasks_appengine_create_task]
  """Create a task for a given queue with an arbitrary payload."""

  from google.cloud import tasks_v2
  from google.protobuf import timestamp_pb2

  # Create a client.
  client = tasks_v2.CloudTasksClient()

  # Construct the fully qualified queue name.
  parent = client.queue_path(project, location, queue)

  # Construct the request body.
  task = {
      'app_engine_http_request': {  # Specify the type of request.
          'http_method': 'POST',
          'relative_uri': relative_handler_uri
      }
  }
  if payload is not None:
    # The API expects a payload of type bytes.
    converted_payload = payload.encode()

    # Add the payload to the request.
    task['app_engine_http_request']['body'] = converted_payload

  if in_seconds is not None:
    # Convert "seconds from now" into an rfc3339 datetime string.
    d = datetime.datetime.utcnow() + datetime.timedelta(seconds=in_seconds)

    # Create Timestamp protobuf.
    timestamp = timestamp_pb2.Timestamp()
    timestamp.FromDatetime(d)

    # Add the timestamp to the tasks.
    task['schedule_time'] = timestamp

  # Use the client to build and send the task.
  response = client.create_task(parent=parent, task=task)
  return response
# [END cloud_tasks_appengine_create_task]
