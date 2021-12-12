# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Duration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time_amount=None, time_unit='minutes'):  # noqa: E501
        """Duration - a model defined in OpenAPI

        :param time_amount: The time_amount of this Duration.  # noqa: E501
        :type time_amount: int
        :param time_unit: The time_unit of this Duration.  # noqa: E501
        :type time_unit: str
        """
        self.openapi_types = {
            'time_amount': int,
            'time_unit': str
        }

        self.attribute_map = {
            'time_amount': 'timeAmount',
            'time_unit': 'timeUnit'
        }

        self._time_amount = time_amount
        self._time_unit = time_unit

    @classmethod
    def from_dict(cls, dikt) -> 'Duration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Duration of this Duration.  # noqa: E501
        :rtype: Duration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time_amount(self):
        """Gets the time_amount of this Duration.


        :return: The time_amount of this Duration.
        :rtype: int
        """
        return self._time_amount

    @time_amount.setter
    def time_amount(self, time_amount):
        """Sets the time_amount of this Duration.


        :param time_amount: The time_amount of this Duration.
        :type time_amount: int
        """
        if time_amount is None:
            raise ValueError("Invalid value for `time_amount`, must not be `None`")  # noqa: E501

        self._time_amount = time_amount

    @property
    def time_unit(self):
        """Gets the time_unit of this Duration.


        :return: The time_unit of this Duration.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this Duration.


        :param time_unit: The time_unit of this Duration.
        :type time_unit: str
        """
        allowed_values = ["days", "hours", "minutes", "seconds", "miliseconds", "micros", "nanos"]  # noqa: E501
        if time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `time_unit` ({0}), must be one of {1}"
                .format(time_unit, allowed_values)
            )

        self._time_unit = time_unit
