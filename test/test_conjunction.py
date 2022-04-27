import unittest
from fattureincloud_python_sdk.filter.condition import Condition
from fattureincloud_python_sdk.filter.conjunction import Conjunction
from fattureincloud_python_sdk.filter.disjunction import Disjunction
from fattureincloud_python_sdk.filter.operator import Operator


class TestConjunction(unittest.TestCase):
    """Conjunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConjunction(self):
        """Test Conjunction"""
        left = Condition(field="city", op=Operator.EQ, value="Bergamo")
        right = Condition(field="age", op=Operator.GTE, value=18)
        conjunction = Conjunction(left, right)
        assert left == conjunction.get_left()
        assert right == conjunction.get_right()
        assert "(city = 'Bergamo' and age >= 18)" == conjunction.build_query()

        left1 = Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991")
        conjunction.set_left(left1)
        assert left1 == conjunction.get_left()
        assert right == conjunction.get_right()
        assert (
            "(team = 'Volley Bergamo 1991' and age >= 18)" == conjunction.build_query()
        )

        right1 = Condition(field="best_player", op=Operator.IS_NOT, value=None)
        conjunction.set_right(right1)
        assert left1 == conjunction.get_left()
        assert right1 == conjunction.get_right()
        assert (
            "(team = 'Volley Bergamo 1991' and best_player is not null)"
            == conjunction.build_query()
        )

    def testEquals(self):
        """Test Equals"""
        conjunction1 = Conjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        conjunction2 = Conjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        assert conjunction1 == conjunction2

        conjunction3 = Conjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        assert conjunction1 != conjunction3

        conjunction4 = Conjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.LT, value="1"),
        )
        assert conjunction1 != conjunction4

        disjunction = Disjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        assert conjunction1 != disjunction


if __name__ == "__main__":
    unittest.main()
