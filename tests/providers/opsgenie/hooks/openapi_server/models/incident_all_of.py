# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class IncidentAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, request_id=None):  # noqa: E501
        """IncidentAllOf - a model defined in OpenAPI

        :param request_id: The request_id of this IncidentAllOf.  # noqa: E501
        :type request_id: str
        """
        self.openapi_types = {
            'request_id': str
        }

        self.attribute_map = {
            'request_id': 'requestId'
        }

        self._request_id = request_id

    @classmethod
    def from_dict(cls, dikt) -> 'IncidentAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Incident_allOf of this IncidentAllOf.  # noqa: E501
        :rtype: IncidentAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request_id(self):
        """Gets the request_id of this IncidentAllOf.


        :return: The request_id of this IncidentAllOf.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this IncidentAllOf.


        :param request_id: The request_id of this IncidentAllOf.
        :type request_id: str
        """

        self._request_id = request_id
