# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.incident_action_payload import IncidentActionPayload
from openapi_server import util

from openapi_server.models.incident_action_payload import IncidentActionPayload  # noqa: E501

class CloseIncidentPayload(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, note=None):  # noqa: E501
        """CloseIncidentPayload - a model defined in OpenAPI

        :param note: The note of this CloseIncidentPayload.  # noqa: E501
        :type note: str
        """
        self.openapi_types = {
            'note': str
        }

        self.attribute_map = {
            'note': 'note'
        }

        self._note = note

    @classmethod
    def from_dict(cls, dikt) -> 'CloseIncidentPayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CloseIncidentPayload of this CloseIncidentPayload.  # noqa: E501
        :rtype: CloseIncidentPayload
        """
        return util.deserialize_model(dikt, cls)

    @property
    def note(self):
        """Gets the note of this CloseIncidentPayload.

        Additional note that will be included with the incident  # noqa: E501

        :return: The note of this CloseIncidentPayload.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this CloseIncidentPayload.

        Additional note that will be included with the incident  # noqa: E501

        :param note: The note of this CloseIncidentPayload.
        :type note: str
        """

        self._note = note
