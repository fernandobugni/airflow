# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.get_account_info_response import GetAccountInfoResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAccountController(BaseTestCase):
    """AccountController integration test stubs"""

    def test_get_info(self):
        """Test case for get_info

        Get Account Info
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/account',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
