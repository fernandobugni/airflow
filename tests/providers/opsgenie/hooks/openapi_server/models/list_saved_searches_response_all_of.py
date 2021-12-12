# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.saved_search_meta import SavedSearchMeta
from openapi_server import util

from openapi_server.models.saved_search_meta import SavedSearchMeta  # noqa: E501

class ListSavedSearchesResponseAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """ListSavedSearchesResponseAllOf - a model defined in OpenAPI

        :param data: The data of this ListSavedSearchesResponseAllOf.  # noqa: E501
        :type data: List[SavedSearchMeta]
        """
        self.openapi_types = {
            'data': List[SavedSearchMeta]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ListSavedSearchesResponseAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListSavedSearchesResponse_allOf of this ListSavedSearchesResponseAllOf.  # noqa: E501
        :rtype: ListSavedSearchesResponseAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListSavedSearchesResponseAllOf.


        :return: The data of this ListSavedSearchesResponseAllOf.
        :rtype: List[SavedSearchMeta]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListSavedSearchesResponseAllOf.


        :param data: The data of this ListSavedSearchesResponseAllOf.
        :type data: List[SavedSearchMeta]
        """

        self._data = data
