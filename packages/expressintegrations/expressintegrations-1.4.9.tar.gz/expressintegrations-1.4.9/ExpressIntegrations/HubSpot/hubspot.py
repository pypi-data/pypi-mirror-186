import json

from ..HTTP import Requests
from datetime import datetime


class hubspot:
    expires_at = None
    access_token = None
    auth_refreshed = False
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    base_url = "https://api.hubapi.com/"

    def __init__(
        self,
        access_token=None,
        expires_at=0,
        client_id=None,
        client_secret=None,
        refresh_token=None
    ):
        self.headers['Authorization'] = f"Bearer {access_token}"
        self.expires_at = expires_at
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.auth_refreshed = False
        self.client_id = client_id
        self.client_secret = client_secret
        if client_id is None:
            raise Exception("Client ID must be provided")
        if client_secret is None:
            raise Exception("Client secret must be provided")

        self.authenticate()

    def authenticate(self):
        if datetime.now().timestamp() > self.expires_at:
            post_url = f"{self.base_url}oauth/v1/token"
            auth_body = {
                'grant_type': 'refresh_token',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'refresh_token': self.refresh_token
            }
            result = Requests.post(post_url, headers=self.auth_headers, data=auth_body)
            auth_result = result['content']
            self.access_token = auth_result['access_token']
            self.headers['Authorization'] = f"Bearer {auth_result['access_token']}"
            self.expires_at = datetime.now().timestamp() + int(auth_result['expires_in'])
            self.auth_refreshed = True

    # Contains utilities for interacting with the HubSpot API
    def get_token_details(self):
        return self.custom_request(
            method='GET',
            endpoint=f"oauth/v1/refresh-tokens/{self.refresh_token}"
        )

    def revoke_token(self):
        post_url = f"{self.base_url}oauth/v1/refresh-tokens/{self.refresh_token}"
        return Requests.delete(post_url, headers=self.auth_headers)

    def custom_request(self, method=None, endpoint=None, **kwargs):
        self.authenticate()
        endpoint = endpoint.lstrip('/')
        post_url = f"{self.base_url}{endpoint}"
        result = Requests.request(method=method, url=post_url, headers=self.headers, **kwargs)
        if result['status_code'] == 401:
            print(f"old headers: {self.headers}")
            self.authenticate()
            print(f"new headers: {self.headers}")
            self.auth_refreshed = True
            result = Requests.request(method=method, url=post_url, headers=self.headers, **kwargs)
        if not Requests.is_success(result['status_code']):
            raise Exception(f"{method} request to {endpoint} failed. Result: {result}")
        return result

    def search_records_by_property_value(
        self,
        object_type,
        property_name,
        property_value,
        property_names=None,
        after=None,
        sorts=None
    ):
        filters = [
            {
                'propertyName': property_name,
                'operator': 'EQ',
                'value': property_value
            }
        ]
        return self.search_records(object_type, property_names, filters, after, sorts)

    def search_records_by_property_known(self, object_type, property_name, property_names, after=None, sorts=None):
        filters = [
            {
                'propertyName': property_name,
                'operator': 'HAS_PROPERTY'
            }
        ]
        return self.search_records(object_type, property_names, filters, after, sorts)

    def search_records_by_property_less_than(
        self,
        object_type,
        property_name,
        property_value,
        property_names,
        after=None,
        sorts=None
    ):
        filters = [
            {
                'propertyName': property_name,
                'operator': 'LT',
                'value': property_value
            }
        ]
        return self.search_records(object_type, property_names, filters, after, sorts)

    def search_records_by_property_greater_than(
        self,
        object_type,
        property_name,
        property_value,
        property_names,
        after=None,
        sorts=None
    ):
        filters = [
            {
                'propertyName': property_name,
                'operator': 'GT',
                'value': property_value
            }
        ]
        return self.search_records(object_type, property_names, filters, after, sorts)

    def search_records_by_property_values(
        self,
        object_type,
        property_name,
        property_values,
        property_names,
        after=None,
        sorts=None
    ):
        filters = [
            {
                'propertyName': property_name,
                'operator': 'IN',
                'values': property_values
            }
        ]
        return self.search_records(object_type, property_names, filters, after, sorts)

    def search_records(self, object_type, property_names, filters, after=None, sorts=None):
        post_body = {
            'filterGroups': [
                {
                    'filters': filters
                }
            ],
            'sorts': sorts,
            'properties': property_names,
            'limit': 100
        }
        if after:
            post_body['after'] = after
        return self.custom_request(
            method='POST',
            endpoint=f"crm/v3/objects/{object_type}/search",
            data=json.dumps(post_body)
        )

    def create_record(self, object_type, properties):
        post_body = {
            'properties': properties
        }
        return self.custom_request(
            method='POST',
            endpoint=f"crm/v3/objects/{object_type}",
            data=json.dumps(post_body)
        )

    def update_record(self, object_id, object_type, properties):
        post_body = {
            'properties': properties
        }
        return self.custom_request(
            method='PATCH',
            endpoint=f"crm/v3/objects/{object_type}/{object_id}?",
            data=json.dumps(post_body)
        )

    def read_records_batch(self, object_type, properties, inputs, id_property=None):
        post_body = {
            'properties': properties,
            'inputs': inputs
        }
        if id_property is not None:
            post_body['idProperty'] = id_property
        return self.custom_request(
            method='POST',
            endpoint=f"crm/v3/objects/{object_type}/batch/read",
            data=json.dumps(post_body)
        )

    def get_record(self, object_type, object_id, property_names=None, associations=None):
        post_url = f"crm/v3/objects/{object_type}/{object_id}?archived=false"
        if property_names:
            post_url = f"{post_url}&properties={'%2C'.join(property_names)}"

        if associations:
            post_url = f"{post_url}&associations={'%2C'.join(associations)}"
        return self.custom_request(
            method='GET',
            endpoint=post_url
        )

    def get_records(self, object_type, property_names=None, associations=None, after=None):
        post_url = f"crm/v3/objects/{object_type}?archived=false&limit=100"
        if property_names:
            post_url = f"{post_url}&properties={'%2C'.join(property_names)}"
        if after is not None:
            post_url = f"{post_url}&after={after}"
        if associations:
            post_url = f"{post_url}&associations={'%2C'.join(associations)}"
        return self.custom_request(
            method='GET',
            endpoint=post_url
        )

    def create_records_batch(self, object_type, records):
        post_body = {
            'inputs': records
        }
        return self.custom_request(
            method='POST',
            endpoint=f"crm/v3/objects/{object_type}/batch/create",
            data=json.dumps(post_body)
        )

    def update_records_batch(self, object_type, records):
        post_body = {
            'inputs': records
        }
        return self.custom_request(
            method='POST',
            endpoint=f"crm/v3/objects/{object_type}/batch/update",
            data=json.dumps(post_body)
        )

    def delete_record(self, object_type, object_id):
        return self.custom_request(
            method='DELETE',
            endpoint=f"crm/v3/objects/{object_type}/{object_id}"
        )

    def get_properties(self, object_type):
        return self.custom_request(
            method='GET',
            endpoint=f"crm/v3/properties/{object_type}?archived=false"
        )

    def get_property(self, object_type, property_name):
        return self.custom_request(
            method='GET',
            endpoint=f"crm/v3/properties/{object_type}/{property_name}?archived=false"
        )

    def update_property(self, object_type, property_name, data):
        acceptable_keys = [
            'groupName',
            'hidden',
            'displayOrder',
            'options',
            'label',
            'type',
            'fieldType',
            'formField'
        ]
        data = {k: v for k, v in data.items() if k in acceptable_keys}
        return self.custom_request(
            method='PATCH',
            endpoint=f"crm/v3/properties/{object_type}/{property_name}",
            data=json.dumps(data)
        )

    def unsubscribe_from_all(self, contact_email):
        post_body = {
            'unsubscribeFromAll': True
        }
        return self.custom_request(
            method='PUT',
            endpoint=f"email/public/v1/subscriptions/{contact_email}",
            data=json.dumps(post_body)
        )

    def get_owner(self, owner_id):
        return self.custom_request(
            method='GET',
            endpoint=f"crm/v3/owners/{owner_id}"
        )

    def search_owners(self, email=None, limit=100, after=None):
        post_url = f"crm/v3/owners?limit={limit}"
        if email is not None:
            post_url = f"{post_url}&email={email}"
        if after is not None:
            post_url = f"{post_url}&after={after}"
        return self.custom_request(
            method='GET',
            endpoint=post_url
        )

    def get_associations(self, from_object_type, to_object_type, from_object_id):
        post_body = {
            'inputs': [
                {
                    'id': from_object_id
                }
            ]
        }
        return self.custom_request(
            method='POST',
            endpoint=f"crm/v3/associations/{from_object_type}/{to_object_type}/batch/read",
            data=json.dumps(post_body)
        )

    def associate(self, from_object_type, from_object_id, to_object_type, to_object_id, association_type):
        return self.custom_request(
            method='PUT',
            endpoint=f"crm/v3/objects/{from_object_type}/{from_object_id}/associations/{to_object_type}/{to_object_id}/{association_type}"
        )

    def dissociate(self, from_object_type, from_object_id, to_object_type, to_object_id, association_type):
        return self.custom_request(
            method='DELETE',
            endpoint=f"crm/v3/objects/{from_object_type}/{from_object_id}/associations/{to_object_type}/{to_object_id}/{association_type}"
        )

    def set_parent_company(self, company_id, parent_company_id):
        return self.associate(
            from_object_type='companies',
            from_object_id=company_id,
            to_object_type='company',
            to_object_id=parent_company_id,
            association_type='CHILD_TO_PARENT_COMPANY'
        )

    def set_child_company(self, company_id, child_company_id):
        return self.associate(
            from_object_type='companies',
            from_object_id=company_id,
            to_object_type='company',
            to_object_id=child_company_id,
            association_type='PARENT_TO_CHILD_COMPANY'
        )

    def set_company_for_contact(self, contact_id, company_id):
        return self.associate(
            from_object_type='contacts',
            from_object_id=contact_id,
            to_object_type='company',
            to_object_id=company_id,
            association_type='CONTACT_TO_COMPANY'
        )

    def set_company_for_deal(self, deal_id, company_id):
        return self.associate(
            from_object_type='deals',
            from_object_id=deal_id,
            to_object_type='company',
            to_object_id=company_id,
            association_type='DEAL_TO_COMPANY'
        )

    def delete_company_from_deal(self, deal_id, company_id):
        return self.dissociate(
            from_object_type='deals',
            from_object_id=deal_id,
            to_object_type='company',
            to_object_id=company_id,
            association_type='DEAL_TO_COMPANY'
        )

    def set_contact_for_deal(self, deal_id, contact_id):
        return self.associate(
            from_object_type='deals',
            from_object_id=deal_id,
            to_object_type='contact',
            to_object_id=contact_id,
            association_type='DEAL_TO_CONTACT'
        )

    def set_deal_for_line_item(self, line_item_id, deal_id):
        return self.associate(
            from_object_type='line_items',
            from_object_id=line_item_id,
            to_object_type='deals',
            to_object_id=deal_id,
            association_type='LINE_ITEM_TO_DEAL'
        )

    def set_contact_for_meeting(self, meeting_id, contact_id):
        return self.associate(
            from_object_type='meetings',
            from_object_id=meeting_id,
            to_object_type='contacts',
            to_object_id=contact_id,
            association_type='MEETING_EVENT_TO_CONTACT'
        )
