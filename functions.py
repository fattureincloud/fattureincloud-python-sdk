import datetime
import json
import sys

from fattureincloud_python_sdk.model.archive_document import ArchiveDocument
from fattureincloud_python_sdk.model.f24 import F24
from fattureincloud_python_sdk.model.f24_status import F24Status
from fattureincloud_python_sdk.model.issued_document import IssuedDocument
from fattureincloud_python_sdk.model.received_document import ReceivedDocument
from fattureincloud_python_sdk.model.issued_document_type import IssuedDocumentType
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.received_document_type import ReceivedDocumentType


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def str_to_class(str):
    return getattr(sys.modules[__name__], str)


def create_from_json(json_str, type):
    json_dict = json.loads(json_str)
    obj = str_to_class(type)
    types_dict = obj.openapi_types
    new_dict = {}
    for key, value in json_dict.items():
        new_dict[key] = cast_to_type(value, types_dict[key][0])
    return obj._from_openapi_data(**new_dict)


def cast_to_type(val, type):
    if type == datetime.date:
        return datetime.datetime.strptime(val, "%Y-%m-%d").date()
    elif type == F24Status:
        return F24Status(val)
    elif type == PaymentAccountType:
        return PaymentAccountType(val)
    elif type == IssuedDocumentType:
        return IssuedDocumentType(val)
    elif type == ReceivedDocumentType:
        return ReceivedDocumentType(val)
    else:
        return val


class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
