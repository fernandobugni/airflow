# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

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
from openapi_server.test import BaseTestCase


class TestAlertController(BaseTestCase):
    """AlertController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_acknowledge_alert(self):
        """Test case for acknowledge_alert

        Acknowledge Alert
        """
        acknowledge_alert_payload = openapi_server.AcknowledgeAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/acknowledge'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(acknowledge_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_add_attachment(self):
        """Test case for add_attachment

        Add Alert Attachment
        """
        query_string = [('alertIdentifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'GenieKey': 'special-key',
        }
        data = dict(file='/path/to/file',
                    user='user_example',
                    index_file='index_file_example')
        response = self.client.open(
            '/v2/alerts/{identifier}/attachments'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_add_details(self):
        """Test case for add_details

        Add Details
        """
        add_details_to_alert_payload = openapi_server.AddDetailsToAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/details'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(add_details_to_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_add_note(self):
        """Test case for add_note

        Add Note
        """
        add_note_to_alert_payload = openapi_server.AddNoteToAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/notes'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(add_note_to_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_add_responder(self):
        """Test case for add_responder

        Add Responder
        """
        add_responder_to_alert_payload = openapi_server.AddResponderToAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/responders'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(add_responder_to_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_add_tags(self):
        """Test case for add_tags

        Add Tags
        """
        add_tags_to_alert_payload = openapi_server.AddTagsToAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/tags'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(add_tags_to_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_add_team(self):
        """Test case for add_team

        Add Team
        """
        add_team_to_alert_payload = openapi_server.AddTeamToAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/teams'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(add_team_to_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_assign_alert(self):
        """Test case for assign_alert

        Assign Alert
        """
        assign_alert_payload = openapi_server.AssignAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/assign'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(assign_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_close_alert(self):
        """Test case for close_alert

        Close Alert
        """
        close_alert_payload = openapi_server.CloseAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/close'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(close_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_count_alerts(self):
        """Test case for count_alerts

        Count Alerts
        """
        query_string = [('query', 'query_example'),
                        ('searchIdentifier', 'search_identifier_example'),
                        ('searchIdentifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/count',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_create_alert(self):
        """Test case for create_alert

        Create Alert
        """
        create_alert_payload = openapi_server.CreateAlertPayload()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts',
            method='POST',
            headers=headers,
            data=json.dumps(create_alert_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_create_saved_searches(self):
        """Test case for create_saved_searches

        Create Saved Search
        """
        create_saved_search_payload = openapi_server.CreateSavedSearchPayload()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/saved-searches',
            method='POST',
            headers=headers,
            data=json.dumps(create_saved_search_payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_alert(self):
        """Test case for delete_alert

        Delete Alert
        """
        query_string = [('identifierType', 'id'),
                        ('user', 'user_example'),
                        ('source', 'source_example')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}'.format(identifier='identifier_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_saved_search(self):
        """Test case for delete_saved_search

        Delete Saved Search
        """
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/saved-searches/{identifier}'.format(identifier='identifier_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_escalate_alert(self):
        """Test case for escalate_alert

        Escalate Alert
        """
        escalate_alert_to_next_payload = openapi_server.EscalateAlertToNextPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/escalate'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(escalate_alert_to_next_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_execute_custom_alert_action(self):
        """Test case for execute_custom_alert_action

        Custom Alert Action
        """
        execute_custom_alert_action_payload = openapi_server.ExecuteCustomAlertActionPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/actions/{action_name}'.format(identifier='identifier_example', action_name='action_name_example'),
            method='POST',
            headers=headers,
            data=json.dumps(execute_custom_alert_action_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_alert(self):
        """Test case for get_alert

        Get Alert
        """
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_attachment(self):
        """Test case for get_attachment

        Get Alert Attachment
        """
        query_string = [('alertIdentifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/attachments/{attachment_id}'.format(identifier='identifier_example', attachment_id=56),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_request_status(self):
        """Test case for get_request_status

        Get Request Status of Alert
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/requests/{request_id}'.format(request_id='request_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_saved_search(self):
        """Test case for get_saved_search

        Get Saved Search
        """
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/saved-searches/{identifier}'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_alerts(self):
        """Test case for list_alerts

        List Alerts
        """
        query_string = [('query', 'query_example'),
                        ('searchIdentifier', 'search_identifier_example'),
                        ('searchIdentifierType', 'id'),
                        ('offset', 56),
                        ('limit', 56),
                        ('sort', 'createdAt'),
                        ('order', 'desc')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_attachments(self):
        """Test case for list_attachments

        List Alert Attachments
        """
        query_string = [('alertIdentifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/attachments'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_logs(self):
        """Test case for list_logs

        List Alert Logs
        """
        query_string = [('identifierType', 'id'),
                        ('offset', 'offset_example'),
                        ('direction', 'next'),
                        ('limit', 56),
                        ('order', 'desc')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/logs'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_notes(self):
        """Test case for list_notes

        List Alert Notes
        """
        query_string = [('identifierType', 'id'),
                        ('offset', 'offset_example'),
                        ('direction', 'next'),
                        ('limit', 56),
                        ('order', 'desc')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/notes'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_recipients(self):
        """Test case for list_recipients

        List Alert Recipients
        """
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/recipients'.format(identifier='identifier_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_saved_searches(self):
        """Test case for list_saved_searches

        Lists Saved Searches
        """
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/saved-searches',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_attachment(self):
        """Test case for remove_attachment

        Remove Alert Attachment
        """
        query_string = [('alertIdentifierType', 'id'),
                        ('user', 'user_example')]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/attachments/{attachment_id}'.format(identifier='identifier_example', attachment_id=56),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_details(self):
        """Test case for remove_details

        Remove Details
        """
        query_string = [('identifierType', 'id'),
                        ('user', 'user_example'),
                        ('note', 'note_example'),
                        ('source', 'source_example'),
                        ('keys', ['keys_example'])]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/details'.format(identifier='identifier_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_tags(self):
        """Test case for remove_tags

        Remove Tags
        """
        query_string = [('identifierType', 'id'),
                        ('user', 'user_example'),
                        ('note', 'note_example'),
                        ('source', 'source_example'),
                        ('tags', ['tags_example'])]
        headers = { 
            'Accept': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/tags'.format(identifier='identifier_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_snooze_alert(self):
        """Test case for snooze_alert

        Snooze Alert
        """
        snooze_alert_payload = openapi_server.SnoozeAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/snooze'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(snooze_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_un_acknowledge_alert(self):
        """Test case for un_acknowledge_alert

        UnAcknowledge Alert
        """
        un_acknowledge_alert_payload = openapi_server.UnAcknowledgeAlertPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/unacknowledge'.format(identifier='identifier_example'),
            method='POST',
            headers=headers,
            data=json.dumps(un_acknowledge_alert_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_alert_description(self):
        """Test case for update_alert_description

        Update Alert Description
        """
        update_alert_description_payload = openapi_server.UpdateAlertDescriptionPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/description'.format(identifier='identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(update_alert_description_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_alert_message(self):
        """Test case for update_alert_message

        Update Alert Message
        """
        update_alert_message_payload = openapi_server.UpdateAlertMessagePayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/message'.format(identifier='identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(update_alert_message_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_alert_priority(self):
        """Test case for update_alert_priority

        Update Alert Priority
        """
        update_alert_priority_payload = openapi_server.UpdateAlertPriorityPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/{identifier}/priority'.format(identifier='identifier_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(update_alert_priority_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_saved_search(self):
        """Test case for update_saved_search

        Update Saved Search
        """
        update_saved_search_payload = openapi_server.UpdateSavedSearchPayload()
        query_string = [('identifierType', 'id')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'GenieKey': 'special-key',
        }
        response = self.client.open(
            '/v2/alerts/saved-searches/{identifier}'.format(identifier='identifier_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(update_saved_search_payload),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
