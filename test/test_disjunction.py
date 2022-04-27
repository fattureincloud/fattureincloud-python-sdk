import unittest
from fattureincloud_python_sdk.filter.condition import Condition
from fattureincloud_python_sdk.filter.conjunction import Conjunction
from fattureincloud_python_sdk.filter.disjunction import Disjunction
from fattureincloud_python_sdk.filter.operator import Operator


class TestDisjunction(unittest.TestCase):
    """Disjunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDisjunction(self):
        """Test Disjunction"""
        left = Condition(field="city", op=Operator.EQ, value="Bergamo")
        right = Condition(field="age", op=Operator.GTE, value=18)
        disjunction = Disjunction(left, right)
        assert left == disjunction.get_left()
        assert right == disjunction.get_right()
        assert "(city = 'Bergamo' or age >= 18)" == disjunction.build_query()

        left1 = Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991")
        disjunction.set_left(left1)
        assert left1 == disjunction.get_left()
        assert right == disjunction.get_right()
        assert (
            "(team = 'Volley Bergamo 1991' or age >= 18)" == disjunction.build_query()
        )

        right1 = Condition(field="best_player", op=Operator.IS_NOT, value=None)
        disjunction.set_right(right1)
        assert left1 == disjunction.get_left()
        assert right1 == disjunction.get_right()
        assert (
            "(team = 'Volley Bergamo 1991' or best_player is not null)"
            == disjunction.build_query()
        )

    def testEquals(self):
        """Test Equals"""
        disjunction1 = Disjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        disjunction2 = Disjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        assert disjunction1 == disjunction2

        disjunction3 = Disjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        assert disjunction1 != disjunction3

        disjunction4 = Disjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.LT, value="1"),
        )
        assert disjunction1 != disjunction4

        conjunction = Conjunction(
            Condition(field="team", op=Operator.EQ, value="Volley Bergamo 1991"),
            Condition(field="position", op=Operator.EQ, value="1"),
        )
        assert disjunction1 != conjunction


if __name__ == "__main__":
    unittest.main()
