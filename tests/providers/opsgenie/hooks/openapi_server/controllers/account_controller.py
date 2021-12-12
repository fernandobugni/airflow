import connexion
import six

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.get_account_info_response import GetAccountInfoResponse  # noqa: E501
from openapi_server import util


def get_info():  # noqa: E501
    """Get Account Info

    Used to search and retrieve account information in OpsGenie # noqa: E501


    :rtype: GetAccountInfoResponse
    """
    return 'do some magic!'
