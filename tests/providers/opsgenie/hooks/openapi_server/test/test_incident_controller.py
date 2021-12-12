# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.close_incident_payload import CloseIncidentPayload  # noqa: E501
from openapi_server.models.create_incident_payload import CreateIncidentPayload  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.get_incident_request_status_response import GetIncidentRequestStatusResponse  # noqa: E501
from openapi_server.models.get_incident_response import GetIncidentResponse  # noqa: E501
from openapi_server.models.list_incidents_response import ListIncidentsResponse  # noqa: E501
from openapi_server.models.success_response import SuccessResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestIncidentController(BaseTestCase):
    """IncidentController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_close_incident(self):
        """Test case for close_incident

        Close Incident
        """
        close_incident_payload = openapi_server.CloseIncidentPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v1/incidents/{identifier}/close'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(close_incident_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_create_incident(self):
        """Test case for create_incident

        Create Incident
        """
        create_incident_payload = openapi_server.CreateIncidentPayload()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v1/incidents/create',
            method='POST',
            headers=headers,
            data=json.dumps(create_incident_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_incident(self):
        """Test case for delete_incident

        Delete Incident
        """
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v1/incidents/{identifier}'.format(identifier='identifier_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_incident(self):
        """Test case for get_incident

        Get Incident
        """
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v1/incidents/{identifier}'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_incident_request_status(self):
        """Test case for get_incident_request_status

        Get Request Status of Incident
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v1/incidents/requests/{request_id}'.format(request_id='request_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_incidents(self):
        """Test case for list_incidents

        List incidents
        """
        query_string = [('query', 'query_example'),
                        ('offset', 56),
                        ('limit', 56),
                        ('sort', 'createdAt'),
                        ('order', 'desc')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v1/incidents/',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
