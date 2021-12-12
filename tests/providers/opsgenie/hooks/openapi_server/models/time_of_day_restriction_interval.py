# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.time_of_day_restriction import TimeOfDayRestriction
from openapi_server.models.time_of_day_restriction_interval_all_of import TimeOfDayRestrictionIntervalAllOf
from openapi_server.models.time_restriction_interval import TimeRestrictionInterval
from openapi_server import util

from openapi_server.models.time_of_day_restriction import TimeOfDayRestriction  # noqa: E501
from openapi_server.models.time_of_day_restriction_interval_all_of import TimeOfDayRestrictionIntervalAllOf  # noqa: E501
from openapi_server.models.time_restriction_interval import TimeRestrictionInterval  # noqa: E501

class TimeOfDayRestrictionInterval(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, restriction=None):  # noqa: E501
        """TimeOfDayRestrictionInterval - a model defined in OpenAPI

        :param type: The type of this TimeOfDayRestrictionInterval.  # noqa: E501
        :type type: str
        :param restriction: The restriction of this TimeOfDayRestrictionInterval.  # noqa: E501
        :type restriction: TimeOfDayRestriction
        """
        self.openapi_types = {
            'type': str,
            'restriction': TimeOfDayRestriction
        }

        self.attribute_map = {
            'type': 'type',
            'restriction': 'restriction'
        }

        self._type = type
        self._restriction = restriction

    @classmethod
    def from_dict(cls, dikt) -> 'TimeOfDayRestrictionInterval':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimeOfDayRestrictionInterval of this TimeOfDayRestrictionInterval.  # noqa: E501
        :rtype: TimeOfDayRestrictionInterval
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this TimeOfDayRestrictionInterval.


        :return: The type of this TimeOfDayRestrictionInterval.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimeOfDayRestrictionInterval.


        :param type: The type of this TimeOfDayRestrictionInterval.
        :type type: str
        """
        allowed_values = ["weekday-and-time-of-day", "time-of-day"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def restriction(self):
        """Gets the restriction of this TimeOfDayRestrictionInterval.


        :return: The restriction of this TimeOfDayRestrictionInterval.
        :rtype: TimeOfDayRestriction
        """
        return self._restriction

    @restriction.setter
    def restriction(self, restriction):
        """Sets the restriction of this TimeOfDayRestrictionInterval.


        :param restriction: The restriction of this TimeOfDayRestrictionInterval.
        :type restriction: TimeOfDayRestriction
        """

        self._restriction = restriction
