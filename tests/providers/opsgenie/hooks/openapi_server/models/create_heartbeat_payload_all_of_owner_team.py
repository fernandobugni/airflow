# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CreateHeartbeatPayloadAllOfOwnerTeam(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, id=None):  # noqa: E501
        """CreateHeartbeatPayloadAllOfOwnerTeam - a model defined in OpenAPI

        :param name: The name of this CreateHeartbeatPayloadAllOfOwnerTeam.  # noqa: E501
        :type name: str
        :param id: The id of this CreateHeartbeatPayloadAllOfOwnerTeam.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'name': str,
            'id': str
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id'
        }

        self._name = name
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'CreateHeartbeatPayloadAllOfOwnerTeam':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateHeartbeatPayload_allOf_ownerTeam of this CreateHeartbeatPayloadAllOfOwnerTeam.  # noqa: E501
        :rtype: CreateHeartbeatPayloadAllOfOwnerTeam
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateHeartbeatPayloadAllOfOwnerTeam.


        :return: The name of this CreateHeartbeatPayloadAllOfOwnerTeam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHeartbeatPayloadAllOfOwnerTeam.


        :param name: The name of this CreateHeartbeatPayloadAllOfOwnerTeam.
        :type name: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this CreateHeartbeatPayloadAllOfOwnerTeam.


        :return: The id of this CreateHeartbeatPayloadAllOfOwnerTeam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateHeartbeatPayloadAllOfOwnerTeam.


        :param id: The id of this CreateHeartbeatPayloadAllOfOwnerTeam.
        :type id: str
        """

        self._id = id
