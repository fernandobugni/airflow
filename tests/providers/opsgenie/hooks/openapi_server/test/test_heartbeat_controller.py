# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.create_heartbeat_payload import CreateHeartbeatPayload  # noqa: E501
from openapi_server.models.create_heartbeat_response import CreateHeartbeatResponse  # noqa: E501
from openapi_server.models.disable_heartbeat_response import DisableHeartbeatResponse  # noqa: E501
from openapi_server.models.enable_heartbeat_response import EnableHeartbeatResponse  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.get_heartbeat_response import GetHeartbeatResponse  # noqa: E501
from openapi_server.models.list_heartbeat_response import ListHeartbeatResponse  # noqa: E501
from openapi_server.models.success_response import SuccessResponse  # noqa: E501
from openapi_server.models.update_heartbeat_payload import UpdateHeartbeatPayload  # noqa: E501
from openapi_server.models.update_heartbeat_response import UpdateHeartbeatResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHeartbeatController(BaseTestCase):
    """HeartbeatController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_create_heartbeat(self):
        """Test case for create_heartbeat

        Create Heartbeat
        """
        create_heartbeat_payload = openapi_server.CreateHeartbeatPayload()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats',
            method='POST',
            headers=headers,
            data=json.dumps(create_heartbeat_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_heartbeat(self):
        """Test case for delete_heartbeat

        Delete Heartbeat
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disable_heartbeat(self):
        """Test case for disable_heartbeat

        Disable Heartbeat
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats/{name}/disable'.format(name='name_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_enable_heartbeat(self):
        """Test case for enable_heartbeat

        Enable Heartbeat
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats/{name}/enable'.format(name='name_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_heartbeat(self):
        """Test case for get_heartbeat

        Get Heartbeat
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_heart_beats(self):
        """Test case for list_heart_beats

        List Heartbeats
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ping(self):
        """Test case for ping

        Ping Heartbeat
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats/{name}/ping'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_heartbeat(self):
        """Test case for update_heartbeat

        Update Heartbeat (Partial)
        """
        update_heartbeat_payload = openapi_server.UpdateHeartbeatPayload()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/heartbeats/{name}'.format(name='name_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(update_heartbeat_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
