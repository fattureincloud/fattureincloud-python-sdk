import unittest
from fattureincloud_python_sdk.filter.condition import Condition
from fattureincloud_python_sdk.filter.operator import Operator


class TestCondition(unittest.TestCase):
    """Condition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCondition(self):
        """Test Condition"""
        condition = Condition(field="name", op=Operator.EQ, value="Mauro")
        assert "name = 'Mauro'" == condition.build_query()

        condition = Condition(field="age", op=Operator.GTE, value=18)
        assert "age >= 18" == condition.build_query()

        condition = Condition(field="ratio", op=Operator.LT, value=3.14)
        assert "ratio < 3.14" == condition.build_query()

        condition = Condition(field="confirmed", op=Operator.NEQ, value=True)
        assert "confirmed <> true" == condition.build_query()

        condition = Condition(field="credit_card", op=Operator.IS_NOT, value=None)
        assert "credit_card is not null" == condition.build_query()

    def testEquals(self):
        """Test Equals"""
        condition = Condition(field="name", op=Operator.EQ, value="Mauro")
        condition1 = Condition(field="name", op=Operator.EQ, value="Mauro")
        assert condition == condition1

        condition2 = Condition(field="cool_name", op=Operator.EQ, value="Mauro")
        assert condition != condition2

        condition3 = Condition(field="name", op=Operator.NEQ, value="Mauro")
        assert condition != condition3

        condition4 = Condition(field="name", op=Operator.EQ, value="Paola")
        assert condition != condition4


if __name__ == "__main__":
    unittest.main()
