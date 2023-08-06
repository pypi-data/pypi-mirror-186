from ..HTTP.Requests import *


class managed_missions:
  def __init__(self, api_key):
    self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
    self.headers['Authorization'] = f"Bearer {api_key}"
    self.base_url = 'https://app.managedmissions.com/API'

  # Contains utilities for interacting with the Managed Missions api
  def get_active_mission_trips(self, **kw):
    post_url = f"{self.base_url}/MissionTripAPI/ActiveTrips"
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve active mission trips. Result: {result}")
    return result

  def get_mission_trips(self, **kw):
    post_url = f"{self.base_url}/MissionTripAPI/List"
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve mission trips. Result: {result}")
    return result

  def get_trip_members(self, mission_trip_id, **kw):
    post_url = f"{self.base_url}/MemberAPI/GetMembersOfTrip"
    kw['MissionTripId'] = mission_trip_id
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve trip members. Result: {result}")
    return result

  def get_people(self, **kw):
    post_url = f"{self.base_url}/PersonAPI/List"
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve people. Result: {result}")
    return result

  def get_person(self, **kw):
    post_url = f"{self.base_url}/PersonAPI/Get"
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve person. Result: {result}")
    return result

  def get_contributions(self, **kw):
    post_url = f"{self.base_url}/ContributionAPI/List"
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve contributions. Result: {result}")
    return result

  def get_donors(self, **kw):
    post_url = f"{self.base_url}/DonorAPI/List"
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve donors. Result: {result}")
    return result

  def get_trip_donors(self, mission_trip_id, **kw):
    post_url = f"{self.base_url}/DonorAPI/GetByMissionTrip"
    kw['missionTripId'] = mission_trip_id
    result = get(post_url, self.headers, params=kw)
    if not Utils.is_success(result['status_code']):
      raise Exception(f"Failed to retrieve trip donors. Result: {result}")
    return result
