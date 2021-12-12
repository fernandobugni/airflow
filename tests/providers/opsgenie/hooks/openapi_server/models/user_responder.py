# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.responder import Responder
from openapi_server.models.user_responder_all_of import UserResponderAllOf
from openapi_server import util

from openapi_server.models.responder import Responder  # noqa: E501
from openapi_server.models.user_responder_all_of import UserResponderAllOf  # noqa: E501

class UserResponder(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, id=None):  # noqa: E501
        """UserResponder - a model defined in OpenAPI

        :param type: The type of this UserResponder.  # noqa: E501
        :type type: str
        :param id: The id of this UserResponder.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'type': str,
            'id': str
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = type
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'UserResponder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserResponder of this UserResponder.  # noqa: E501
        :rtype: UserResponder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this UserResponder.


        :return: The type of this UserResponder.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserResponder.


        :param type: The type of this UserResponder.
        :type type: str
        """
        allowed_values = ["user", "team", "escalation", "schedule"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this UserResponder.


        :return: The id of this UserResponder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserResponder.


        :param id: The id of this UserResponder.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id
