# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.list_heartbeat_response_all_of_data import ListHeartbeatResponseAllOfData
from openapi_server import util

from openapi_server.models.list_heartbeat_response_all_of_data import ListHeartbeatResponseAllOfData  # noqa: E501

class ListHeartbeatResponseAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """ListHeartbeatResponseAllOf - a model defined in OpenAPI

        :param data: The data of this ListHeartbeatResponseAllOf.  # noqa: E501
        :type data: ListHeartbeatResponseAllOfData
        """
        self.openapi_types = {
            'data': ListHeartbeatResponseAllOfData
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ListHeartbeatResponseAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListHeartbeatResponse_allOf of this ListHeartbeatResponseAllOf.  # noqa: E501
        :rtype: ListHeartbeatResponseAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListHeartbeatResponseAllOf.


        :return: The data of this ListHeartbeatResponseAllOf.
        :rtype: ListHeartbeatResponseAllOfData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListHeartbeatResponseAllOf.


        :param data: The data of this ListHeartbeatResponseAllOf.
        :type data: ListHeartbeatResponseAllOfData
        """

        self._data = data
