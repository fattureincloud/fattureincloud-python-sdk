import unittest
from fattureincloud_python_sdk.filter.operator import Operator


class TestOperator(unittest.TestCase):
    """Operator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOperator(self):
        """Test Operator"""
        assert "=" == Operator.EQ.value

        assert ">" == Operator.GT.value

        assert ">=" == Operator.GTE.value

        assert "<" == Operator.LT.value

        assert "<=" == Operator.LTE.value

        assert "<>" == Operator.NEQ.value

        assert "is" == Operator.IS.value

        assert "is not" == Operator.IS_NOT.value

        assert "like" == Operator.LIKE.value

        assert "contains" == Operator.CONTAINS.value

        assert "starts with" == Operator.STARTS_WITH.value

        assert "ends with" == Operator.ENDS_WITH.value


if __name__ == "__main__":
    unittest.main()
