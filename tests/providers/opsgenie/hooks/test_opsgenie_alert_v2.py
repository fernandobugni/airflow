import connexion
import pytest
from airflow.providers.opsgenie.hooks.opsgenie_alert_v2 import OpsgenieAlertHookV2
from openapi_server import encoder

import threading


@pytest.fixture(autouse=True)
def mock_server():
    app = connexion.App(__name__, specification_dir='./')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Python SDK for Opsgenie REST API'},
                pythonic_params=True)

    server_thread = threading.Thread(target=app.run, name="Mock server", kwargs={'port': '8080'})
    server_thread.daemon = True
    server_thread.start()

    import time
    time.sleep(2)  # This sleep is to be sure that server could finish starting up

    yield server_thread


def test_list_alert(mock_server):
    hook = OpsgenieAlertHookV2(api_key='123', host='http://0.0.0.0:8080')
    alerts = hook.list_alerts()
    print(alerts)

    print("test_list_alert")
