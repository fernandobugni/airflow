# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.heartbeat_meta import HeartbeatMeta
from openapi_server import util

from openapi_server.models.heartbeat_meta import HeartbeatMeta  # noqa: E501

class DisableHeartbeatResponseAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """DisableHeartbeatResponseAllOf - a model defined in OpenAPI

        :param data: The data of this DisableHeartbeatResponseAllOf.  # noqa: E501
        :type data: HeartbeatMeta
        """
        self.openapi_types = {
            'data': HeartbeatMeta
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'DisableHeartbeatResponseAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DisableHeartbeatResponse_allOf of this DisableHeartbeatResponseAllOf.  # noqa: E501
        :rtype: DisableHeartbeatResponseAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this DisableHeartbeatResponseAllOf.


        :return: The data of this DisableHeartbeatResponseAllOf.
        :rtype: HeartbeatMeta
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DisableHeartbeatResponseAllOf.


        :param data: The data of this DisableHeartbeatResponseAllOf.
        :type data: HeartbeatMeta
        """

        self._data = data
