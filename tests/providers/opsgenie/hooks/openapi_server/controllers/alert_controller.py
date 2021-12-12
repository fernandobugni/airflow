import connexion
import six

from openapi_server.models.acknowledge_alert_payload import AcknowledgeAlertPayload  # noqa: E501
from openapi_server.models.add_details_to_alert_payload import AddDetailsToAlertPayload  # noqa: E501
from openapi_server.models.add_note_to_alert_payload import AddNoteToAlertPayload  # noqa: E501
from openapi_server.models.add_responder_to_alert_payload import AddResponderToAlertPayload  # noqa: E501
from openapi_server.models.add_tags_to_alert_payload import AddTagsToAlertPayload  # noqa: E501
from openapi_server.models.add_team_to_alert_payload import AddTeamToAlertPayload  # noqa: E501
from openapi_server.models.assign_alert_payload import AssignAlertPayload  # noqa: E501
from openapi_server.models.close_alert_payload import CloseAlertPayload  # noqa: E501
from openapi_server.models.create_alert_payload import CreateAlertPayload  # noqa: E501
from openapi_server.models.create_saved_search_payload import CreateSavedSearchPayload  # noqa: E501
from openapi_server.models.create_saved_search_response import CreateSavedSearchResponse  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.escalate_alert_to_next_payload import EscalateAlertToNextPayload  # noqa: E501
from openapi_server.models.execute_custom_alert_action_payload import ExecuteCustomAlertActionPayload  # noqa: E501
from openapi_server.models.get_alert_attachment_response import GetAlertAttachmentResponse  # noqa: E501
from openapi_server.models.get_alert_response import GetAlertResponse  # noqa: E501
from openapi_server.models.get_count_alerts_response import GetCountAlertsResponse  # noqa: E501
from openapi_server.models.get_request_status_response import GetRequestStatusResponse  # noqa: E501
from openapi_server.models.get_saved_search_response import GetSavedSearchResponse  # noqa: E501
from openapi_server.models.list_alert_attachments_response import ListAlertAttachmentsResponse  # noqa: E501
from openapi_server.models.list_alert_logs_response import ListAlertLogsResponse  # noqa: E501
from openapi_server.models.list_alert_notes_response import ListAlertNotesResponse  # noqa: E501
from openapi_server.models.list_alert_recipients_response import ListAlertRecipientsResponse  # noqa: E501
from openapi_server.models.list_alerts_response import ListAlertsResponse  # noqa: E501
from openapi_server.models.list_saved_searches_response import ListSavedSearchesResponse  # noqa: E501
from openapi_server.models.snooze_alert_payload import SnoozeAlertPayload  # noqa: E501
from openapi_server.models.success_response import SuccessResponse  # noqa: E501
from openapi_server.models.un_acknowledge_alert_payload import UnAcknowledgeAlertPayload  # noqa: E501
from openapi_server.models.update_alert_description_payload import UpdateAlertDescriptionPayload  # noqa: E501
from openapi_server.models.update_alert_message_payload import UpdateAlertMessagePayload  # noqa: E501
from openapi_server.models.update_alert_priority_payload import UpdateAlertPriorityPayload  # noqa: E501
from openapi_server.models.update_saved_search_payload import UpdateSavedSearchPayload  # noqa: E501
from openapi_server import util


def acknowledge_alert(identifier, identifier_type=None, acknowledge_alert_payload=None):  # noqa: E501
    """Acknowledge Alert

    Acknowledges alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param acknowledge_alert_payload: Request payload of acknowledging alert action
    :type acknowledge_alert_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        acknowledge_alert_payload = AcknowledgeAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_attachment(identifier, file, alert_identifier_type=None, user=None, index_file=None):  # noqa: E501
    """Add Alert Attachment

    Add Alert Attachment to related alert # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param file: Attachment file to be uploaded
    :type file: str
    :param alert_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type alert_identifier_type: str
    :param user: Display name of the request owner
    :type user: str
    :param index_file: Name of html file which will be shown when attachment clicked on UI
    :type index_file: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def add_details(identifier, add_details_to_alert_payload, identifier_type=None):  # noqa: E501
    """Add Details

    Add details to the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param add_details_to_alert_payload: Request payload of adding alert details action
    :type add_details_to_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        add_details_to_alert_payload = AddDetailsToAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_note(identifier, add_note_to_alert_payload, identifier_type=None):  # noqa: E501
    """Add Note

    Adds note to alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param add_note_to_alert_payload: Request payload of adding note to alert action
    :type add_note_to_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        add_note_to_alert_payload = AddNoteToAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_responder(identifier, add_responder_to_alert_payload, identifier_type=None):  # noqa: E501
    """Add Responder

    Add responder to alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param add_responder_to_alert_payload: Request payload of adding responder to alert action
    :type add_responder_to_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        add_responder_to_alert_payload = AddResponderToAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_tags(identifier, add_tags_to_alert_payload, identifier_type=None):  # noqa: E501
    """Add Tags

    Add tags to the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param add_tags_to_alert_payload: Request payload of creating alert tags action
    :type add_tags_to_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        add_tags_to_alert_payload = AddTagsToAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_team(identifier, add_team_to_alert_payload, identifier_type=None):  # noqa: E501
    """Add Team

    Add team to alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param add_team_to_alert_payload: Request payload of adding team to alert action
    :type add_team_to_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        add_team_to_alert_payload = AddTeamToAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def assign_alert(identifier, assign_alert_payload, identifier_type=None):  # noqa: E501
    """Assign Alert

    Assign alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param assign_alert_payload: Request payload of assigning alert action
    :type assign_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        assign_alert_payload = AssignAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def close_alert(identifier, identifier_type=None, close_alert_payload=None):  # noqa: E501
    """Close Alert

    Closes alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param close_alert_payload: Request payload of closing alert action
    :type close_alert_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        close_alert_payload = CloseAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def count_alerts(query=None, search_identifier=None, search_identifier_type=None):  # noqa: E501
    """Count Alerts

    Count alerts in Opsgenie # noqa: E501

    :param query: Search query to apply while filtering the alerts
    :type query: str
    :param search_identifier: Identifier of the saved search query to apply while filtering the alerts
    :type search_identifier: str
    :param search_identifier_type: Identifier type of the saved search query. Possible values are id and name. Default value is id. If searchIdentifier is not provided, this value is ignored.
    :type search_identifier_type: str

    :rtype: GetCountAlertsResponse
    """
    return 'do some magic!'


def create_alert(create_alert_payload):  # noqa: E501
    """Create Alert

    Creates a new alert # noqa: E501

    :param create_alert_payload: Request payload of created alert
    :type create_alert_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        create_alert_payload = CreateAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_saved_searches(create_saved_search_payload):  # noqa: E501
    """Create Saved Search

    Create saved search with given fields # noqa: E501

    :param create_saved_search_payload: Request payload of creating saved search
    :type create_saved_search_payload: dict | bytes

    :rtype: CreateSavedSearchResponse
    """
    if connexion.request.is_json:
        create_saved_search_payload = CreateSavedSearchPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_alert(identifier, identifier_type=None, user=None, source=None):  # noqa: E501
    """Delete Alert

    Deletes an alert using alert id, tiny id or alias # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param user: Display name of the request owner
    :type user: str
    :param source: Display name of the request source
    :type source: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def delete_saved_search(identifier, identifier_type=None):  # noqa: E501
    """Delete Saved Search

    Deletes saved search using given search identifier # noqa: E501

    :param identifier: Identifier of the saved search which could be &#39;id&#39; or &#39;name&#39;
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, or &#39;name&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def escalate_alert(identifier, escalate_alert_to_next_payload, identifier_type=None):  # noqa: E501
    """Escalate Alert

    Escalate alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param escalate_alert_to_next_payload: Request payload of escalating alert action
    :type escalate_alert_to_next_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        escalate_alert_to_next_payload = EscalateAlertToNextPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def execute_custom_alert_action(identifier, action_name, identifier_type=None, execute_custom_alert_action_payload=None):  # noqa: E501
    """Custom Alert Action

    Custom actions for the alert # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param action_name: Name of the action to execute
    :type action_name: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param execute_custom_alert_action_payload: Request payload of executing custom alert action
    :type execute_custom_alert_action_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        execute_custom_alert_action_payload = ExecuteCustomAlertActionPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_alert(identifier, identifier_type=None):  # noqa: E501
    """Get Alert

    Returns alert with given id, tiny id or alias # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: GetAlertResponse
    """
    return 'do some magic!'


def get_attachment(identifier, attachment_id, alert_identifier_type=None):  # noqa: E501
    """Get Alert Attachment

    Get alert attachment name and url for the given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param attachment_id: Identifier of alert attachment
    :type attachment_id: int
    :param alert_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type alert_identifier_type: str

    :rtype: GetAlertAttachmentResponse
    """
    return 'do some magic!'


def get_request_status(request_id):  # noqa: E501
    """Get Request Status of Alert

    Used to track the status and alert details (if any) of the request whose identifier is given # noqa: E501

    :param request_id: Universally unique identifier of the questioned request
    :type request_id: str

    :rtype: GetRequestStatusResponse
    """
    return 'do some magic!'


def get_saved_search(identifier, identifier_type=None):  # noqa: E501
    """Get Saved Search

    Get saved search for the given search identifier # noqa: E501

    :param identifier: Identifier of the saved search which could be &#39;id&#39; or &#39;name&#39;
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, or &#39;name&#39;
    :type identifier_type: str

    :rtype: GetSavedSearchResponse
    """
    return 'do some magic!'


def list_alerts(query=None, search_identifier=None, search_identifier_type=None, offset=None, limit=None, sort=None, order=None):  # noqa: E501
    """List Alerts

    Returns list of alerts # noqa: E501

    :param query: Search query to apply while filtering the alerts
    :type query: str
    :param search_identifier: Identifier of the saved search query to apply while filtering the alerts
    :type search_identifier: str
    :param search_identifier_type: Identifier type of the saved search query. Possible values are &#39;id&#39;, or &#39;name&#39;
    :type search_identifier_type: str
    :param offset: Start index of the result set (to apply pagination). Minimum value (and also default value) is 0
    :type offset: int
    :param limit: Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100
    :type limit: int
    :param sort: Name of the field that result set will be sorted by
    :type sort: str
    :param order: Sorting order of the result set
    :type order: str

    :rtype: ListAlertsResponse
    """
    #return 'do some magic! babe'
    return {
            "data": [
                {
                    "id": "70413a06-38d6-4c85-92b8-5ebc900d42e2",
                    "tinyId": "1791",
                    "alias": "event_573",
                    "message": "Our servers are in danger",
                    "status": "closed",
                    "acknowledged": False,
                    "isSeen": True,
                    "tags": [
                        "OverwriteQuietHours",
                        "Critical"
                    ],
                    "snoozed": True,
                    "snoozedUntil": "2017-04-03T20:32:35.143Z",
                    "count": 79,
                    "lastOccurredAt": "2017-04-03T20:05:50.894Z",
                    "createdAt": "2017-03-21T20:32:52.353Z",
                    "updatedAt": "2017-04-03T20:32:57.301Z",
                    "source": "Isengard",
                    "owner": "morpheus@opsgenie.com",
                    "priority": "P4",
                    "responders":[
                      {
                          "id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c",
                          "type":"team"
                      },
                      {
                          "id":"bb4d9938-c3c2-455d-aaab-727aa701c0d8",
                          "type":"user"
                      },
                      {
                          "id":"aee8a0de-c80f-4515-a232-501c0bc9d715",
                          "type":"escalation"
                      },
                      {
                          "id":"80564037-1984-4f38-b98e-8a1f662df552",
                          "type":"schedule"
                      }
                    ],
                    "integration": {
                        "id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c",
                        "name": "Nebuchadnezzar",
                        "type": "API"
                    },
                    "report": {
                        "ackTime": 15702,
                        "closeTime": 60503,
                        "acknowledgedBy": "agent_smith@opsgenie.com",
                        "closedBy": "neo@opsgenie.com"
                    }
                },
                {
                    "id": "70413a06-38d6-4c85-92b8-5ebc900d42e2",
                    "tinyId": "1791",
                    "alias": "event_573",
                    "message": "Sample Message",
                    "status": "open",
                    "acknowledged": False,
                    "isSeen": False,
                    "tags": [
                        "RandomTag"
                    ],
                    "snoozed": False,
                    "count": 1,
                    "lastOccurredAt": "2017-03-21T20:32:52.353Z",
                    "createdAt": "2017-03-21T20:32:52.353Z",
                    "updatedAt": "2017-04-03T20:32:57.301Z",
                    "source": "Zion",
                    "owner": "",
                    "priority": "P5",
                    "responders":[],
                    "integration": {
                        "id": "4513b7ea-3b91-b7e4-438f-e3e54af9147c",
                        "name": "My_Lovely_Amazon",
                        "type": "CloudWatch"
                    }
                }

            ],
            "paging":{
                "next":"https://api.opsgenie.com/v2/alerts?query=status%3Aopen&offset=20&limit=10&sort=createdAt&order=desc",
                "first":"https://api.opsgenie.com/v2/alerts?query=status%3Aopen&offset=0&limit=10&sort=createdAt&order=desc",
                "last":"https://api.opsgenie.com/v2/alerts?query=status%3Aopen&offset=100&limit=10&sort=createdAt&order=desc"
            },
            "took": 0.605,
            "requestId": "9ae63dd7-ed00-4c81-86f0-c4ffd33142c9"
        }

def list_attachments(identifier, alert_identifier_type=None):  # noqa: E501
    """List Alert Attachments

    List alert attachment names and urls for related alert # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param alert_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type alert_identifier_type: str

    :rtype: ListAlertAttachmentsResponse
    """
    return 'do some magic!'


def list_logs(identifier, identifier_type=None, offset=None, direction=None, limit=None, order=None):  # noqa: E501
    """List Alert Logs

    List alert logs for the given alert identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param offset: Starting value of the offset property
    :type offset: str
    :param direction: Page direction to apply for the given offset with &#39;next&#39; and &#39;prev&#39;
    :type direction: str
    :param limit: Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100
    :type limit: int
    :param order: Sorting order of the result set
    :type order: str

    :rtype: ListAlertLogsResponse
    """
    return 'do some magic!'


def list_notes(identifier, identifier_type=None, offset=None, direction=None, limit=None, order=None):  # noqa: E501
    """List Alert Notes

    List alert notes for the given alert identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param offset: Starting value of the offset property
    :type offset: str
    :param direction: Page direction to apply for the given offset with &#39;next&#39; and &#39;prev&#39;
    :type direction: str
    :param limit: Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100
    :type limit: int
    :param order: Sorting order of the result set
    :type order: str

    :rtype: ListAlertNotesResponse
    """
    return 'do some magic!'


def list_recipients(identifier, identifier_type=None):  # noqa: E501
    """List Alert Recipients

    List alert recipients for the given alert identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: ListAlertRecipientsResponse
    """
    return 'do some magic!'


def list_saved_searches():  # noqa: E501
    """Lists Saved Searches

    List all saved searches # noqa: E501


    :rtype: ListSavedSearchesResponse
    """
    return 'do some magic!'


def remove_attachment(identifier, attachment_id, alert_identifier_type=None, user=None):  # noqa: E501
    """Remove Alert Attachment

    Remove alert attachment for the given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param attachment_id: Identifier of alert attachment
    :type attachment_id: int
    :param alert_identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type alert_identifier_type: str
    :param user: Display name of the request owner
    :type user: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def remove_details(identifier, keys, identifier_type=None, user=None, note=None, source=None):  # noqa: E501
    """Remove Details

    Remove details of the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param keys: Comma separated list of keys to remove from the custom properties of the alert (e.g. &#39;key1,key2&#39;)
    :type keys: List[str]
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param user: Display name of the request owner
    :type user: str
    :param note: Additional alert note to add
    :type note: str
    :param source: Display name of the request source
    :type source: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def remove_tags(identifier, tags, identifier_type=None, user=None, note=None, source=None):  # noqa: E501
    """Remove Tags

    Remove tags of the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param tags: Tags field of the given alert as comma seperated values (e.g. &#39;tag1, tag2&#39;)
    :type tags: List[str]
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param user: Display name of the request owner
    :type user: str
    :param note: Additional alert note to add
    :type note: str
    :param source: Display name of the request source
    :type source: str

    :rtype: SuccessResponse
    """
    return 'do some magic!'


def snooze_alert(identifier, snooze_alert_payload, identifier_type=None):  # noqa: E501
    """Snooze Alert

    Snooze alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param snooze_alert_payload: Request payload of snoozing alert action
    :type snooze_alert_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        snooze_alert_payload = SnoozeAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def un_acknowledge_alert(identifier, identifier_type=None, un_acknowledge_alert_payload=None):  # noqa: E501
    """UnAcknowledge Alert

    UnAcknowledge alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str
    :param un_acknowledge_alert_payload: Request payload of unacknowledging alert action
    :type un_acknowledge_alert_payload: dict | bytes

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        un_acknowledge_alert_payload = UnAcknowledgeAlertPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_alert_description(identifier, update_alert_description_payload, identifier_type=None):  # noqa: E501
    """Update Alert Description

    Update the description of the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param update_alert_description_payload: Request payload of update alert description
    :type update_alert_description_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        update_alert_description_payload = UpdateAlertDescriptionPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_alert_message(identifier, update_alert_message_payload, identifier_type=None):  # noqa: E501
    """Update Alert Message

    Update the message of the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param update_alert_message_payload: Request payload of update alert message
    :type update_alert_message_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        update_alert_message_payload = UpdateAlertMessagePayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_alert_priority(identifier, update_alert_priority_payload, identifier_type=None):  # noqa: E501
    """Update Alert Priority

    Update the priority of the alert with given identifier # noqa: E501

    :param identifier: Identifier of alert which could be alert id, tiny id or alert alias
    :type identifier: str
    :param update_alert_priority_payload: Request payload of update alert priority
    :type update_alert_priority_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, &#39;alias&#39; or &#39;tiny&#39;
    :type identifier_type: str

    :rtype: SuccessResponse
    """
    if connexion.request.is_json:
        update_alert_priority_payload = UpdateAlertPriorityPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_saved_search(identifier, update_saved_search_payload, identifier_type=None):  # noqa: E501
    """Update Saved Search

    Update saved search for the given search identifier # noqa: E501

    :param identifier: Identifier of the saved search which could be &#39;id&#39; or &#39;name&#39;
    :type identifier: str
    :param update_saved_search_payload: Request payload of updating saved search
    :type update_saved_search_payload: dict | bytes
    :param identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39;, or &#39;name&#39;
    :type identifier_type: str

    :rtype: GetSavedSearchResponse
    """
    if connexion.request.is_json:
        update_saved_search_payload = UpdateSavedSearchPayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
