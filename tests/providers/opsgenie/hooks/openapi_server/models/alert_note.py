# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AlertNote(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, note=None, owner=None, created_at=None, offset=None):  # noqa: E501
        """AlertNote - a model defined in OpenAPI

        :param note: The note of this AlertNote.  # noqa: E501
        :type note: str
        :param owner: The owner of this AlertNote.  # noqa: E501
        :type owner: str
        :param created_at: The created_at of this AlertNote.  # noqa: E501
        :type created_at: datetime
        :param offset: The offset of this AlertNote.  # noqa: E501
        :type offset: str
        """
        self.openapi_types = {
            'note': str,
            'owner': str,
            'created_at': datetime,
            'offset': str
        }

        self.attribute_map = {
            'note': 'note',
            'owner': 'owner',
            'created_at': 'createdAt',
            'offset': 'offset'
        }

        self._note = note
        self._owner = owner
        self._created_at = created_at
        self._offset = offset

    @classmethod
    def from_dict(cls, dikt) -> 'AlertNote':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlertNote of this AlertNote.  # noqa: E501
        :rtype: AlertNote
        """
        return util.deserialize_model(dikt, cls)

    @property
    def note(self):
        """Gets the note of this AlertNote.


        :return: The note of this AlertNote.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AlertNote.


        :param note: The note of this AlertNote.
        :type note: str
        """

        self._note = note

    @property
    def owner(self):
        """Gets the owner of this AlertNote.


        :return: The owner of this AlertNote.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AlertNote.


        :param owner: The owner of this AlertNote.
        :type owner: str
        """

        self._owner = owner

    @property
    def created_at(self):
        """Gets the created_at of this AlertNote.


        :return: The created_at of this AlertNote.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AlertNote.


        :param created_at: The created_at of this AlertNote.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def offset(self):
        """Gets the offset of this AlertNote.


        :return: The offset of this AlertNote.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this AlertNote.


        :param offset: The offset of this AlertNote.
        :type offset: str
        """

        self._offset = offset
