# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alert_action_payload import AlertActionPayload
from openapi_server import util

from openapi_server.models.alert_action_payload import AlertActionPayload  # noqa: E501

class AddNoteToAlertPayload(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user=None, note=None, source=None):  # noqa: E501
        """AddNoteToAlertPayload - a model defined in OpenAPI

        :param user: The user of this AddNoteToAlertPayload.  # noqa: E501
        :type user: str
        :param note: The note of this AddNoteToAlertPayload.  # noqa: E501
        :type note: str
        :param source: The source of this AddNoteToAlertPayload.  # noqa: E501
        :type source: str
        """
        self.openapi_types = {
            'user': str,
            'note': str,
            'source': str
        }

        self.attribute_map = {
            'user': 'user',
            'note': 'note',
            'source': 'source'
        }

        self._user = user
        self._note = note
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'AddNoteToAlertPayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddNoteToAlertPayload of this AddNoteToAlertPayload.  # noqa: E501
        :rtype: AddNoteToAlertPayload
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user(self):
        """Gets the user of this AddNoteToAlertPayload.

        Display name of the request owner  # noqa: E501

        :return: The user of this AddNoteToAlertPayload.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AddNoteToAlertPayload.

        Display name of the request owner  # noqa: E501

        :param user: The user of this AddNoteToAlertPayload.
        :type user: str
        """

        self._user = user

    @property
    def note(self):
        """Gets the note of this AddNoteToAlertPayload.

        Additional note that will be added while creating the alert  # noqa: E501

        :return: The note of this AddNoteToAlertPayload.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AddNoteToAlertPayload.

        Additional note that will be added while creating the alert  # noqa: E501

        :param note: The note of this AddNoteToAlertPayload.
        :type note: str
        """

        self._note = note

    @property
    def source(self):
        """Gets the source of this AddNoteToAlertPayload.

        Source field of the alert. Default value is IP address of the incoming request  # noqa: E501

        :return: The source of this AddNoteToAlertPayload.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AddNoteToAlertPayload.

        Source field of the alert. Default value is IP address of the incoming request  # noqa: E501

        :param source: The source of this AddNoteToAlertPayload.
        :type source: str
        """

        self._source = source
