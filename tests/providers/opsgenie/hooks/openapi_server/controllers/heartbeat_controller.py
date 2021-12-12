import connexion
import six

from openapi_server.models.create_heartbeat_payload import CreateHeartbeatPayload  # noqa: E501
from openapi_server.models.create_heartbeat_response import CreateHeartbeatResponse  # noqa: E501
from openapi_server.models.disable_heartbeat_response import DisableHeartbeatResponse  # noqa: E501
from openapi_server.models.enable_heartbeat_response import EnableHeartbeatResponse  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.get_heartbeat_response import GetHeartbeatResponse  # noqa: E501
from openapi_server.models.list_heartbeat_response import ListHeartbeatResponse  # noqa: E501
from openapi_server.models.success_response import SuccessResponse  # noqa: E501
from openapi_server.models.update_heartbeat_payload import UpdateHeartbeatPayload  # noqa: E501
from openapi_server.models.update_heartbeat_response import UpdateHeartbeatResponse  # noqa: E501
from openapi_server import util


def create_heartbeat(create_heartbeat_payload):  # noqa: E501
    """Create Heartbeat

    Create a new heartbeat # noqa: E501

    :param create_heartbeat_payload: Request payload of created heartbeat
    :type create_heartbeat_payload: dict | bytes

    :rtype: CreateHeartbeatResponse
    """
    if connexion.request.is_json:
        create_heartbeat_payload = CreateHeartbeatPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_heartbeat(name):  # noqa: E501
    """Delete Heartbeat

    Delete heartbeat with given name # noqa: E501

    :param name: Name of the heartbeat
    :type name: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def disable_heartbeat(name):  # noqa: E501
    """Disable Heartbeat

    Disable heartbeat request with given name # noqa: E501

    :param name: Name of the heartbeat
    :type name: str

    :rtype: DisableHeartbeatResponse
    """
    return 'do some magic!'


def enable_heartbeat(name):  # noqa: E501
    """Enable Heartbeat

    Enable heartbeat request with given name # noqa: E501

    :param name: Name of the heartbeat
    :type name: str

    :rtype: EnableHeartbeatResponse
    """
    return 'do some magic!'


def get_heartbeat(name):  # noqa: E501
    """Get Heartbeat

    Returns heartbeat with given name # noqa: E501

    :param name: Name of the heartbeat
    :type name: str

    :rtype: GetHeartbeatResponse
    """
    return 'do some magic!'


def list_heart_beats():  # noqa: E501
    """List Heartbeats

    Returns list of Heartbeats # noqa: E501


    :rtype: ListHeartbeatResponse
    """
    return 'do some magic!'


def ping(name):  # noqa: E501
    """Ping Heartbeat

    Ping Heartbeat for given heartbeat name # noqa: E501

    :param name: Name of the heartbeat
    :type name: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def update_heartbeat(name, update_heartbeat_payload=None):  # noqa: E501
    """Update Heartbeat (Partial)

    Update Heartbeatwith given name # noqa: E501

    :param name: Name of the heartbeat
    :type name: str
    :param update_heartbeat_payload: Request payload of update heartbeat action
    :type update_heartbeat_payload: dict | bytes

    :rtype: UpdateHeartbeatResponse
    """
    if connexion.request.is_json:
        update_heartbeat_payload = UpdateHeartbeatPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
