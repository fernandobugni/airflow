# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Heartbeat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, interval=None, enabled=None, interval_unit=None, expired=None, last_ping_time=None):  # noqa: E501
        """Heartbeat - a model defined in OpenAPI

        :param name: The name of this Heartbeat.  # noqa: E501
        :type name: str
        :param description: The description of this Heartbeat.  # noqa: E501
        :type description: str
        :param interval: The interval of this Heartbeat.  # noqa: E501
        :type interval: int
        :param enabled: The enabled of this Heartbeat.  # noqa: E501
        :type enabled: bool
        :param interval_unit: The interval_unit of this Heartbeat.  # noqa: E501
        :type interval_unit: str
        :param expired: The expired of this Heartbeat.  # noqa: E501
        :type expired: bool
        :param last_ping_time: The last_ping_time of this Heartbeat.  # noqa: E501
        :type last_ping_time: datetime
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'interval': int,
            'enabled': bool,
            'interval_unit': str,
            'expired': bool,
            'last_ping_time': datetime
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'interval': 'interval',
            'enabled': 'enabled',
            'interval_unit': 'intervalUnit',
            'expired': 'expired',
            'last_ping_time': 'lastPingTime'
        }

        self._name = name
        self._description = description
        self._interval = interval
        self._enabled = enabled
        self._interval_unit = interval_unit
        self._expired = expired
        self._last_ping_time = last_ping_time

    @classmethod
    def from_dict(cls, dikt) -> 'Heartbeat':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Heartbeat of this Heartbeat.  # noqa: E501
        :rtype: Heartbeat
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Heartbeat.


        :return: The name of this Heartbeat.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Heartbeat.


        :param name: The name of this Heartbeat.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Heartbeat.


        :return: The description of this Heartbeat.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Heartbeat.


        :param description: The description of this Heartbeat.
        :type description: str
        """

        self._description = description

    @property
    def interval(self):
        """Gets the interval of this Heartbeat.


        :return: The interval of this Heartbeat.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Heartbeat.


        :param interval: The interval of this Heartbeat.
        :type interval: int
        """

        self._interval = interval

    @property
    def enabled(self):
        """Gets the enabled of this Heartbeat.


        :return: The enabled of this Heartbeat.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Heartbeat.


        :param enabled: The enabled of this Heartbeat.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def interval_unit(self):
        """Gets the interval_unit of this Heartbeat.


        :return: The interval_unit of this Heartbeat.
        :rtype: str
        """
        return self._interval_unit

    @interval_unit.setter
    def interval_unit(self, interval_unit):
        """Sets the interval_unit of this Heartbeat.


        :param interval_unit: The interval_unit of this Heartbeat.
        :type interval_unit: str
        """
        allowed_values = ["minutes", "hours", "days"]  # noqa: E501
        if interval_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `interval_unit` ({0}), must be one of {1}"
                .format(interval_unit, allowed_values)
            )

        self._interval_unit = interval_unit

    @property
    def expired(self):
        """Gets the expired of this Heartbeat.


        :return: The expired of this Heartbeat.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this Heartbeat.


        :param expired: The expired of this Heartbeat.
        :type expired: bool
        """

        self._expired = expired

    @property
    def last_ping_time(self):
        """Gets the last_ping_time of this Heartbeat.


        :return: The last_ping_time of this Heartbeat.
        :rtype: datetime
        """
        return self._last_ping_time

    @last_ping_time.setter
    def last_ping_time(self, last_ping_time):
        """Sets the last_ping_time of this Heartbeat.


        :param last_ping_time: The last_ping_time of this Heartbeat.
        :type last_ping_time: datetime
        """

        self._last_ping_time = last_ping_time
