# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TimeOfDayRestriction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start_hour=None, start_min=None, end_hour=None, end_min=None):  # noqa: E501
        """TimeOfDayRestriction - a model defined in OpenAPI

        :param start_hour: The start_hour of this TimeOfDayRestriction.  # noqa: E501
        :type start_hour: int
        :param start_min: The start_min of this TimeOfDayRestriction.  # noqa: E501
        :type start_min: int
        :param end_hour: The end_hour of this TimeOfDayRestriction.  # noqa: E501
        :type end_hour: int
        :param end_min: The end_min of this TimeOfDayRestriction.  # noqa: E501
        :type end_min: int
        """
        self.openapi_types = {
            'start_hour': int,
            'start_min': int,
            'end_hour': int,
            'end_min': int
        }

        self.attribute_map = {
            'start_hour': 'startHour',
            'start_min': 'startMin',
            'end_hour': 'endHour',
            'end_min': 'endMin'
        }

        self._start_hour = start_hour
        self._start_min = start_min
        self._end_hour = end_hour
        self._end_min = end_min

    @classmethod
    def from_dict(cls, dikt) -> 'TimeOfDayRestriction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimeOfDayRestriction of this TimeOfDayRestriction.  # noqa: E501
        :rtype: TimeOfDayRestriction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start_hour(self):
        """Gets the start_hour of this TimeOfDayRestriction.


        :return: The start_hour of this TimeOfDayRestriction.
        :rtype: int
        """
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        """Sets the start_hour of this TimeOfDayRestriction.


        :param start_hour: The start_hour of this TimeOfDayRestriction.
        :type start_hour: int
        """

        self._start_hour = start_hour

    @property
    def start_min(self):
        """Gets the start_min of this TimeOfDayRestriction.


        :return: The start_min of this TimeOfDayRestriction.
        :rtype: int
        """
        return self._start_min

    @start_min.setter
    def start_min(self, start_min):
        """Sets the start_min of this TimeOfDayRestriction.


        :param start_min: The start_min of this TimeOfDayRestriction.
        :type start_min: int
        """

        self._start_min = start_min

    @property
    def end_hour(self):
        """Gets the end_hour of this TimeOfDayRestriction.


        :return: The end_hour of this TimeOfDayRestriction.
        :rtype: int
        """
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        """Sets the end_hour of this TimeOfDayRestriction.


        :param end_hour: The end_hour of this TimeOfDayRestriction.
        :type end_hour: int
        """

        self._end_hour = end_hour

    @property
    def end_min(self):
        """Gets the end_min of this TimeOfDayRestriction.


        :return: The end_min of this TimeOfDayRestriction.
        :rtype: int
        """
        return self._end_min

    @end_min.setter
    def end_min(self, end_min):
        """Sets the end_min of this TimeOfDayRestriction.


        :param end_min: The end_min of this TimeOfDayRestriction.
        :type end_min: int
        """

        self._end_min = end_min
