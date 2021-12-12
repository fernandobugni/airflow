# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.base_incident import BaseIncident
from openapi_server.models.page_details import PageDetails
from openapi_server import util

from openapi_server.models.base_incident import BaseIncident  # noqa: E501
from openapi_server.models.page_details import PageDetails  # noqa: E501

class ListIncidentsResponseAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None, paging=None):  # noqa: E501
        """ListIncidentsResponseAllOf - a model defined in OpenAPI

        :param data: The data of this ListIncidentsResponseAllOf.  # noqa: E501
        :type data: List[BaseIncident]
        :param paging: The paging of this ListIncidentsResponseAllOf.  # noqa: E501
        :type paging: PageDetails
        """
        self.openapi_types = {
            'data': List[BaseIncident],
            'paging': PageDetails
        }

        self.attribute_map = {
            'data': 'data',
            'paging': 'paging'
        }

        self._data = data
        self._paging = paging

    @classmethod
    def from_dict(cls, dikt) -> 'ListIncidentsResponseAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListIncidentsResponse_allOf of this ListIncidentsResponseAllOf.  # noqa: E501
        :rtype: ListIncidentsResponseAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListIncidentsResponseAllOf.


        :return: The data of this ListIncidentsResponseAllOf.
        :rtype: List[BaseIncident]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListIncidentsResponseAllOf.


        :param data: The data of this ListIncidentsResponseAllOf.
        :type data: List[BaseIncident]
        """

        self._data = data

    @property
    def paging(self):
        """Gets the paging of this ListIncidentsResponseAllOf.


        :return: The paging of this ListIncidentsResponseAllOf.
        :rtype: PageDetails
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this ListIncidentsResponseAllOf.


        :param paging: The paging of this ListIncidentsResponseAllOf.
        :type paging: PageDetails
        """

        self._paging = paging
