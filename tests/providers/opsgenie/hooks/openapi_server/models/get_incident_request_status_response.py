# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.base_response import BaseResponse
from openapi_server.models.get_incident_request_status_response_all_of import GetIncidentRequestStatusResponseAllOf
from openapi_server.models.incident_request_status import IncidentRequestStatus
from openapi_server import util

from openapi_server.models.base_response import BaseResponse  # noqa: E501
from openapi_server.models.get_incident_request_status_response_all_of import GetIncidentRequestStatusResponseAllOf  # noqa: E501
from openapi_server.models.incident_request_status import IncidentRequestStatus  # noqa: E501

class GetIncidentRequestStatusResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, request_id=None, took=0.0, data=None):  # noqa: E501
        """GetIncidentRequestStatusResponse - a model defined in OpenAPI

        :param request_id: The request_id of this GetIncidentRequestStatusResponse.  # noqa: E501
        :type request_id: str
        :param took: The took of this GetIncidentRequestStatusResponse.  # noqa: E501
        :type took: float
        :param data: The data of this GetIncidentRequestStatusResponse.  # noqa: E501
        :type data: IncidentRequestStatus
        """
        self.openapi_types = {
            'request_id': str,
            'took': float,
            'data': IncidentRequestStatus
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
    def from_dict(cls, dikt) -> 'GetIncidentRequestStatusResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetIncidentRequestStatusResponse of this GetIncidentRequestStatusResponse.  # noqa: E501
        :rtype: GetIncidentRequestStatusResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request_id(self):
        """Gets the request_id of this GetIncidentRequestStatusResponse.


        :return: The request_id of this GetIncidentRequestStatusResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetIncidentRequestStatusResponse.


        :param request_id: The request_id of this GetIncidentRequestStatusResponse.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def took(self):
        """Gets the took of this GetIncidentRequestStatusResponse.


        :return: The took of this GetIncidentRequestStatusResponse.
        :rtype: float
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this GetIncidentRequestStatusResponse.


        :param took: The took of this GetIncidentRequestStatusResponse.
        :type took: float
        """
        if took is None:
            raise ValueError("Invalid value for `took`, must not be `None`")  # noqa: E501

        self._took = took

    @property
    def data(self):
        """Gets the data of this GetIncidentRequestStatusResponse.


        :return: The data of this GetIncidentRequestStatusResponse.
        :rtype: IncidentRequestStatus
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetIncidentRequestStatusResponse.


        :param data: The data of this GetIncidentRequestStatusResponse.
        :type data: IncidentRequestStatus
        """

        self._data = data
