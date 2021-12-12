from __future__ import print_function
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint

from airflow.hooks.base import BaseHook


class OpsgenieAlertHookV2(BaseHook):

    def __init__(self, api_key: str, host: str):
        super().__init__()
        self.configuration = opsgenie_sdk.configuration.Configuration()
        self.configuration.api_key['Authorization'] = api_key

        if host is not None:
            self.configuration.api_key['host'] = host
            self.configuration.host = host

        self.configuration.debug = False
        self.configuration.retry_count = 1
        self.configuration.retry_http_response = ['4xx', '5xx']
        self.configuration.retry_delay = 0
        self.configuration.retry_enabled = False

        self.api_client = opsgenie_sdk.api_client.ApiClient(configuration=self.configuration)

    def list_alerts(self):
        api_instance = opsgenie_sdk.AlertApi(api_client=self.api_client)

        try:
            api_response = api_instance.list_alerts()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AlertApi->get_alert: %s\n" % e)

        return api_response
