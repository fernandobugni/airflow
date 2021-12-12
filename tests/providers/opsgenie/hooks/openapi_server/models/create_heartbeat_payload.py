# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.create_heartbeat_payload_all_of import CreateHeartbeatPayloadAllOf
from openapi_server.models.create_heartbeat_payload_all_of_owner_team import CreateHeartbeatPayloadAllOfOwnerTeam
from openapi_server import util

from openapi_server.models.create_heartbeat_payload_all_of import CreateHeartbeatPayloadAllOf  # noqa: E501
from openapi_server.models.create_heartbeat_payload_all_of_owner_team import CreateHeartbeatPayloadAllOfOwnerTeam  # noqa: E501

class CreateHeartbeatPayload(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, interval=None, interval_unit=None, enabled=None, owner_team=None, alert_message=None, alert_tags=None, alert_priority=None):  # noqa: E501
        """CreateHeartbeatPayload - a model defined in OpenAPI

        :param name: The name of this CreateHeartbeatPayload.  # noqa: E501
        :type name: str
        :param description: The description of this CreateHeartbeatPayload.  # noqa: E501
        :type description: str
        :param interval: The interval of this CreateHeartbeatPayload.  # noqa: E501
        :type interval: int
        :param interval_unit: The interval_unit of this CreateHeartbeatPayload.  # noqa: E501
        :type interval_unit: str
        :param enabled: The enabled of this CreateHeartbeatPayload.  # noqa: E501
        :type enabled: bool
        :param owner_team: The owner_team of this CreateHeartbeatPayload.  # noqa: E501
        :type owner_team: CreateHeartbeatPayloadAllOfOwnerTeam
        :param alert_message: The alert_message of this CreateHeartbeatPayload.  # noqa: E501
        :type alert_message: str
        :param alert_tags: The alert_tags of this CreateHeartbeatPayload.  # noqa: E501
        :type alert_tags: List[str]
        :param alert_priority: The alert_priority of this CreateHeartbeatPayload.  # noqa: E501
        :type alert_priority: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'interval': int,
            'interval_unit': str,
            'enabled': bool,
            'owner_team': CreateHeartbeatPayloadAllOfOwnerTeam,
            'alert_message': str,
            'alert_tags': List[str],
            'alert_priority': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'interval': 'interval',
            'interval_unit': 'intervalUnit',
            'enabled': 'enabled',
            'owner_team': 'ownerTeam',
            'alert_message': 'alertMessage',
            'alert_tags': 'alertTags',
            'alert_priority': 'alertPriority'
        }

        self._name = name
        self._description = description
        self._interval = interval
        self._interval_unit = interval_unit
        self._enabled = enabled
        self._owner_team = owner_team
        self._alert_message = alert_message
        self._alert_tags = alert_tags
        self._alert_priority = alert_priority

    @classmethod
    def from_dict(cls, dikt) -> 'CreateHeartbeatPayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateHeartbeatPayload of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: CreateHeartbeatPayload
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateHeartbeatPayload.

        Name of the heartbeat  # noqa: E501

        :return: The name of this CreateHeartbeatPayload.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHeartbeatPayload.

        Name of the heartbeat  # noqa: E501

        :param name: The name of this CreateHeartbeatPayload.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateHeartbeatPayload.

        An optional description of the heartbeat  # noqa: E501

        :return: The description of this CreateHeartbeatPayload.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHeartbeatPayload.

        An optional description of the heartbeat  # noqa: E501

        :param description: The description of this CreateHeartbeatPayload.
        :type description: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")  # noqa: E501

        self._description = description

    @property
    def interval(self):
        """Gets the interval of this CreateHeartbeatPayload.

        Specifies how often a heartbeat message should be expected  # noqa: E501

        :return: The interval of this CreateHeartbeatPayload.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreateHeartbeatPayload.

        Specifies how often a heartbeat message should be expected  # noqa: E501

        :param interval: The interval of this CreateHeartbeatPayload.
        :type interval: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501
        if interval is not None and interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._interval = interval

    @property
    def interval_unit(self):
        """Gets the interval_unit of this CreateHeartbeatPayload.

        Interval specified as 'minutes', 'hours' or 'days'  # noqa: E501

        :return: The interval_unit of this CreateHeartbeatPayload.
        :rtype: str
        """
        return self._interval_unit

    @interval_unit.setter
    def interval_unit(self, interval_unit):
        """Sets the interval_unit of this CreateHeartbeatPayload.

        Interval specified as 'minutes', 'hours' or 'days'  # noqa: E501

        :param interval_unit: The interval_unit of this CreateHeartbeatPayload.
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
    def enabled(self):
        """Gets the enabled of this CreateHeartbeatPayload.

        Enable/disable heartbeat monitoring  # noqa: E501

        :return: The enabled of this CreateHeartbeatPayload.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateHeartbeatPayload.

        Enable/disable heartbeat monitoring  # noqa: E501

        :param enabled: The enabled of this CreateHeartbeatPayload.
        :type enabled: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def owner_team(self):
        """Gets the owner_team of this CreateHeartbeatPayload.


        :return: The owner_team of this CreateHeartbeatPayload.
        :rtype: CreateHeartbeatPayloadAllOfOwnerTeam
        """
        return self._owner_team

    @owner_team.setter
    def owner_team(self, owner_team):
        """Sets the owner_team of this CreateHeartbeatPayload.


        :param owner_team: The owner_team of this CreateHeartbeatPayload.
        :type owner_team: CreateHeartbeatPayloadAllOfOwnerTeam
        """

        self._owner_team = owner_team

    @property
    def alert_message(self):
        """Gets the alert_message of this CreateHeartbeatPayload.

        Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is 'HeartbeatName is expired'  # noqa: E501

        :return: The alert_message of this CreateHeartbeatPayload.
        :rtype: str
        """
        return self._alert_message

    @alert_message.setter
    def alert_message(self, alert_message):
        """Sets the alert_message of this CreateHeartbeatPayload.

        Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is 'HeartbeatName is expired'  # noqa: E501

        :param alert_message: The alert_message of this CreateHeartbeatPayload.
        :type alert_message: str
        """
        if alert_message is not None and len(alert_message) > 130:
            raise ValueError("Invalid value for `alert_message`, length must be less than or equal to `130`")  # noqa: E501

        self._alert_message = alert_message

    @property
    def alert_tags(self):
        """Gets the alert_tags of this CreateHeartbeatPayload.

        Specifies the alert tags for heartbeat expiration alert  # noqa: E501

        :return: The alert_tags of this CreateHeartbeatPayload.
        :rtype: List[str]
        """
        return self._alert_tags

    @alert_tags.setter
    def alert_tags(self, alert_tags):
        """Sets the alert_tags of this CreateHeartbeatPayload.

        Specifies the alert tags for heartbeat expiration alert  # noqa: E501

        :param alert_tags: The alert_tags of this CreateHeartbeatPayload.
        :type alert_tags: List[str]
        """
        if alert_tags is not None and len(alert_tags) > 20:
            raise ValueError("Invalid value for `alert_tags`, number of items must be less than or equal to `20`")  # noqa: E501

        self._alert_tags = alert_tags

    @property
    def alert_priority(self):
        """Gets the alert_priority of this CreateHeartbeatPayload.

        Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3  # noqa: E501

        :return: The alert_priority of this CreateHeartbeatPayload.
        :rtype: str
        """
        return self._alert_priority

    @alert_priority.setter
    def alert_priority(self, alert_priority):
        """Sets the alert_priority of this CreateHeartbeatPayload.

        Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3  # noqa: E501

        :param alert_priority: The alert_priority of this CreateHeartbeatPayload.
        :type alert_priority: str
        """
        allowed_values = ["P1", "P2", "P3", "P4", "P5"]  # noqa: E501
        if alert_priority not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_priority` ({0}), must be one of {1}"
                .format(alert_priority, allowed_values)
            )

        self._alert_priority = alert_priority
