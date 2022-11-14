# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from fattureincloud_python_sdk.api.archive_api import ArchiveApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from fattureincloud_python_sdk.api.archive_api import ArchiveApi
from fattureincloud_python_sdk.api.cashbook_api import CashbookApi
from fattureincloud_python_sdk.api.clients_api import ClientsApi
from fattureincloud_python_sdk.api.companies_api import CompaniesApi
from fattureincloud_python_sdk.api.emails_api import EmailsApi
from fattureincloud_python_sdk.api.info_api import InfoApi
from fattureincloud_python_sdk.api.issued_documents_api import IssuedDocumentsApi
from fattureincloud_python_sdk.api.issued_e_invoices_api import IssuedEInvoicesApi
from fattureincloud_python_sdk.api.products_api import ProductsApi
from fattureincloud_python_sdk.api.receipts_api import ReceiptsApi
from fattureincloud_python_sdk.api.received_documents_api import ReceivedDocumentsApi
from fattureincloud_python_sdk.api.settings_api import SettingsApi
from fattureincloud_python_sdk.api.suppliers_api import SuppliersApi
from fattureincloud_python_sdk.api.taxes_api import TaxesApi
from fattureincloud_python_sdk.api.user_api import UserApi
