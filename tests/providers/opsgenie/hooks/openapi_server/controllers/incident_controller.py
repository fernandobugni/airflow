import connexion
import six

from openapi_server.models.close_incident_payload import CloseIncidentPayload  # noqa: E501
from openapi_server.models.create_incident_payload import CreateIncidentPayload  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.get_incident_request_status_response import GetIncidentRequestStatusResponse  # noqa: E501
from openapi_server.models.get_incident_response import GetIncidentResponse  # noqa: E501
from openapi_server.models.list_incidents_response import ListIncidentsResponse  # noqa: E501
from openapi_server.models.success_response import SuccessResponse  # noqa: E501
from openapi_server import util


def close_incident(identifier, identifier_type=None, close_incident_payload=None):  # noqa: E501
    """Close Incident

    Closes incident with given identifier # noqa: E501

    :param identifier: Identifier of incident which could be incident id or tiny id
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;tiny. Default is id&#39;
    :type identifier_type: str
    :param close_incident_payload: Request payload of closing incident action
    :type close_incident_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        close_incident_payload = CloseIncidentPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_incident(create_incident_payload):  # noqa: E501
    """Create Incident

    Creates a new incident # noqa: E501

    :param create_incident_payload: Request payload of created incident
    :type create_incident_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        create_incident_payload = CreateIncidentPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_incident(identifier, identifier_type=None):  # noqa: E501
    """Delete Incident

    Deletes an incident using incident id or the tiny id # noqa: E501

    :param identifier: Identifier of incident which could be incident id or tiny id
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;tiny. Default is id&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def get_incident(identifier, identifier_type=None):  # noqa: E501
    """Get Incident

    Returns incident with given id, tiny id or alias # noqa: E501

    :param identifier: Identifier of incident which could be incident id or tiny id
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;tiny. Default is id&#39;
    :type identifier_type: str

    :rtype: GetIncidentResponse
    """
    return 'do some magic!'


def get_incident_request_status(request_id):  # noqa: E501
    """Get Request Status of Incident

    Used to track the status and incident details (if any) of the request whose identifier is given # noqa: E501

    :param request_id: Universally unique identifier of the questioned request
    :type request_id: str

    :rtype: GetIncidentRequestStatusResponse
    """
    return 'do some magic!'


def list_incidents(query, offset=None, limit=None, sort=None, order=None):  # noqa: E501
    """List incidents

    Return list of incidents # noqa: E501

    :param query: Search query to apply while filtering the incidents.
    :type query: str
    :param offset: Start index of the result set (to apply pagination). Minimum value (and also default value) is 0.
    :type offset: int
    :param limit: Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100
    :type limit: int
    :param sort: Name of the field that result set will be sorted by
    :type sort: str
    :param order: Sorting order of the result set
    :type order: str

    :rtype: ListIncidentsResponse
    """
    return 'do some magic!'
