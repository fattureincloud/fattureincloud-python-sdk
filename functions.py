import datetime
import json
import sys

from fattureincloud_python_sdk.models.archive_document import ArchiveDocument
from fattureincloud_python_sdk.models.f24 import F24
from fattureincloud_python_sdk.models.f24_status import F24Status
from fattureincloud_python_sdk.models.issued_document import IssuedDocument
from fattureincloud_python_sdk.models.received_document import ReceivedDocument
from fattureincloud_python_sdk.models.issued_document_type import IssuedDocumentType
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.models.received_document_type import ReceivedDocumentType


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def str_to_class(str):
    return getattr(sys.modules[__name__], str)


def create_from_json(json_str, type):
    return str_to_class(type).from_json(json_str)


class Dict2Class(object):
    def __init__(self, my_dict):

        for key in my_dict:
            setattr(self, key, my_dict[key])
