import unittest

from fattureincloud_python_sdk.oauth2.scopes import Scope


class TestScope(unittest.TestCase):
    """Filter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScope(self):
        scope = Scope.ISSUED_DOCUMENTS_CREDIT_NOTE_ALL
        assert scope.value == 'issued_documents.credit_note:a'


if __name__ == '__main__':
    unittest.main()
