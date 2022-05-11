import unittest

from fattureincloud_python_sdk.filter.condition import Condition
from fattureincloud_python_sdk.filter.conjunction import Conjunction
from fattureincloud_python_sdk.filter.disjunction import Disjunction
from fattureincloud_python_sdk.filter.filter import Filter
from fattureincloud_python_sdk.filter.operator import Operator


class TestFilter(unittest.TestCase):
    """Filter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFilter(self):
        """Test Filter"""
        filter = Filter()
        assert None == filter.get_expression()

        condition = Condition("surname", Operator.EQ, "Cooper")
        filter = Filter(condition)
        assert condition == filter.get_expression()

        condition1 = Condition("name", Operator.EQ, "Sheldon Lee")
        filter.set_expression(condition1)
        assert condition1 == filter.get_expression()

    def testWhereCondition(self):
        """Test WhereCondition"""
        filter = Filter()
        assert None == filter.get_expression()

        condition = Condition("surname", Operator.EQ, "Cooper")
        filter.where_condition("surname", Operator.EQ, "Cooper")
        assert condition == filter.get_expression()

        condition1 = Condition("name", Operator.EQ, "Sheldon Lee")
        filter.where_condition("name", Operator.EQ, "Sheldon Lee")
        assert condition1 == filter.get_expression()

    def testWhereExpression(self):
        """Test WhereExpression"""
        filter = Filter()
        assert None == filter.get_expression()

        condition = Condition("surname", Operator.EQ, "Cooper")
        filter.where_expression(condition)
        assert condition == filter.get_expression()

        condition1 = Condition("name", Operator.EQ, "Sheldon Lee")
        filter.where_expression(condition1)
        assert condition1 == filter.get_expression()

    def testAndCondition(self):
        """Test AndCondition"""
        filter = Filter()
        assert None == filter.get_expression()

        condition1 = Condition("surname", Operator.EQ, "Cooper")
        condition2 = Condition("name", Operator.EQ, "Sheldon Lee")
        conjunction = Conjunction(condition1, condition2)

        with self.assertRaises(Exception):
            filter.and_condition("name", Operator.EQ, "Sheldon Lee")

        filter.where_condition("surname", Operator.EQ, "Cooper").and_condition(
            "name", Operator.EQ, "Sheldon Lee"
        )

        assert conjunction == filter.get_expression()

    def testAndExpression(self):
        """Test AndExpression"""
        filter = Filter()
        assert None == filter.get_expression()

        condition1 = Condition("surname", Operator.EQ, "Cooper")
        condition2 = Condition("name", Operator.EQ, "Sheldon Lee")
        conjunction = Conjunction(condition1, condition2)

        with self.assertRaises(Exception):
            filter.and_expression(condition2)

        filter.where_expression(condition1)
        with self.assertRaises(Exception):
            filter.and_expression(None)

        filter.and_expression(condition2)

        assert conjunction == filter.get_expression()

    def testAndFilter(self):
        """Test AndFilter"""
        filter = Filter()
        assert None == filter.get_expression()

        condition1 = Condition("surname", Operator.EQ, "Cooper")
        condition2 = Condition("name", Operator.EQ, "Sheldon Lee")
        conjunction = Conjunction(condition1, condition2)

        with self.assertRaises(Exception):
            filter.and_filter(Filter(condition2))

        filter.where_expression(condition1)
        with self.assertRaises(Exception):
            filter.and_filter(Filter())

        with self.assertRaises(Exception):
            filter.and_filter(None)

        filter.and_filter(Filter(condition2))

        assert conjunction == filter.get_expression()

    def testOrCondition(self):
        """Test OrCondition"""
        filter = Filter()
        assert None == filter.get_expression()

        condition1 = Condition("surname", Operator.EQ, "Cooper")
        condition2 = Condition("name", Operator.EQ, "Sheldon Lee")
        disjunction = Disjunction(condition1, condition2)

        with self.assertRaises(Exception):
            filter.or_condition("name", Operator.EQ, "Sheldon Lee")

        filter.where_condition("surname", Operator.EQ, "Cooper").or_condition(
            "name", Operator.EQ, "Sheldon Lee"
        )

        assert disjunction == filter.get_expression()

    def testOrExpression(self):
        """Test OrExpression"""
        filter = Filter()
        assert None == filter.get_expression()

        condition1 = Condition("surname", Operator.EQ, "Cooper")
        condition2 = Condition("name", Operator.EQ, "Sheldon Lee")
        disjunction = Disjunction(condition1, condition2)

        with self.assertRaises(Exception):
            filter.or_expression(condition2)

        filter.where_expression(condition1)
        with self.assertRaises(Exception):
            filter.or_expression(None)

        filter.or_expression(condition2)

        assert disjunction == filter.get_expression()

    def testOrFilter(self):
        """Test OrFilter"""
        filter = Filter()
        assert None == filter.get_expression()

        condition1 = Condition("surname", Operator.EQ, "Cooper")
        condition2 = Condition("name", Operator.EQ, "Sheldon Lee")
        disjunction = Disjunction(condition1, condition2)

        with self.assertRaises(Exception):
            filter.or_filter(Filter(condition2))

        filter.where_expression(condition1)
        with self.assertRaises(Exception):
            filter.or_filter(Filter())

        with self.assertRaises(Exception):
            filter.or_filter(None)

        filter.or_filter(Filter(condition2))

        assert disjunction == filter.get_expression()

    def testBuildQuery(self):
        """Test BuildQuery"""
        filter = Filter()
        assert None == filter.get_expression()
        assert "" == filter.build_query()

        condition = Condition("surname", Operator.EQ, "Cooper")
        filter.where_expression(condition)

        assert "surname = 'Cooper'" == filter.build_query()

    def testBuildUrlEncodedQuery(self):
        """Test BuildUrlEncodedQuery"""
        filter = Filter()
        assert None == filter.get_expression()
        assert "" == filter.build_query()

        condition = Condition("surname", Operator.EQ, "Cooper")
        filter.where_expression(condition)

        assert "surname+%3D+%27Cooper%27" == filter.build_url_encoded_query()

    def testEquals(self):
        """Test Equals"""
        filter1 = Filter().where_condition(
            field="name", op=Operator.EQ, value="Sheldon Lee"
        )
        filter2 = Filter().where_condition(
            field="name", op=Operator.EQ, value="Sheldon Lee"
        )
        assert filter1 == filter2

        filter3 = Filter().where_condition(field="name", op=Operator.EQ, value="Penny")
        assert filter1 != filter3


if __name__ == "__main__":
    unittest.main()
