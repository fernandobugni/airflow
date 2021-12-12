# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.weekday_time_restriction import WeekdayTimeRestriction
from openapi_server import util

from openapi_server.models.weekday_time_restriction import WeekdayTimeRestriction  # noqa: E501

class WeekdayTimeRestrictionIntervalAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, restrictions=None):  # noqa: E501
        """WeekdayTimeRestrictionIntervalAllOf - a model defined in OpenAPI

        :param restrictions: The restrictions of this WeekdayTimeRestrictionIntervalAllOf.  # noqa: E501
        :type restrictions: List[WeekdayTimeRestriction]
        """
        self.openapi_types = {
            'restrictions': List[WeekdayTimeRestriction]
        }

        self.attribute_map = {
            'restrictions': 'restrictions'
        }

        self._restrictions = restrictions

    @classmethod
    def from_dict(cls, dikt) -> 'WeekdayTimeRestrictionIntervalAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WeekdayTimeRestrictionInterval_allOf of this WeekdayTimeRestrictionIntervalAllOf.  # noqa: E501
        :rtype: WeekdayTimeRestrictionIntervalAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def restrictions(self):
        """Gets the restrictions of this WeekdayTimeRestrictionIntervalAllOf.


        :return: The restrictions of this WeekdayTimeRestrictionIntervalAllOf.
        :rtype: List[WeekdayTimeRestriction]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this WeekdayTimeRestrictionIntervalAllOf.


        :param restrictions: The restrictions of this WeekdayTimeRestrictionIntervalAllOf.
        :type restrictions: List[WeekdayTimeRestriction]
        """
        if restrictions is not None and len(restrictions) > 15:
            raise ValueError("Invalid value for `restrictions`, number of items must be less than or equal to `15`")  # noqa: E501
        if restrictions is not None and len(restrictions) < 1:
            raise ValueError("Invalid value for `restrictions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._restrictions = restrictions
