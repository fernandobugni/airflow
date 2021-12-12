# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.account_info import AccountInfo
from openapi_server.models.base_response import BaseResponse
from openapi_server.models.get_account_info_response_all_of import GetAccountInfoResponseAllOf
from openapi_server import util

from openapi_server.models.account_info import AccountInfo  # noqa: E501
from openapi_server.models.base_response import BaseResponse  # noqa: E501
from openapi_server.models.get_account_info_response_all_of import GetAccountInfoResponseAllOf  # noqa: E501

class GetAccountInfoResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, request_id=None, took=0.0, data=None):  # noqa: E501
        """GetAccountInfoResponse - a model defined in OpenAPI

        :param request_id: The request_id of this GetAccountInfoResponse.  # noqa: E501
        :type request_id: str
        :param took: The took of this GetAccountInfoResponse.  # noqa: E501
        :type took: float
        :param data: The data of this GetAccountInfoResponse.  # noqa: E501
        :type data: AccountInfo
        """
        self.openapi_types = {
            'request_id': str,
            'took': float,
            'data': AccountInfo
        }

        self.attribute_map = {
            'request_id': 'requestId',
            'took': 'took',
            'data': 'data'
        }

        self._request_id = request_id
        self._took = took
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'GetAccountInfoResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetAccountInfoResponse of this GetAccountInfoResponse.  # noqa: E501
        :rtype: GetAccountInfoResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request_id(self):
        """Gets the request_id of this GetAccountInfoResponse.


        :return: The request_id of this GetAccountInfoResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetAccountInfoResponse.


        :param request_id: The request_id of this GetAccountInfoResponse.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def took(self):
        """Gets the took of this GetAccountInfoResponse.


        :return: The took of this GetAccountInfoResponse.
        :rtype: float
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this GetAccountInfoResponse.


        :param took: The took of this GetAccountInfoResponse.
        :type took: float
        """
        if took is None:
            raise ValueError("Invalid value for `took`, must not be `None`")  # noqa: E501

        self._took = took

    @property
    def data(self):
        """Gets the data of this GetAccountInfoResponse.


        :return: The data of this GetAccountInfoResponse.
        :rtype: AccountInfo
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetAccountInfoResponse.


        :param data: The data of this GetAccountInfoResponse.
        :type data: AccountInfo
        """

        self._data = data
