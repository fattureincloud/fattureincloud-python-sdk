import urllib.parse

from fattureincloud_python_sdk.filter.condition import Condition
from fattureincloud_python_sdk.filter.conjunction import Conjunction
from fattureincloud_python_sdk.filter.disjunction import Disjunction
from fattureincloud_python_sdk.filter.expression import Expression
from fattureincloud_python_sdk.filter.operator import Operator


class Filter:
    def __init__(self, expression: Expression = None):
        self.__expression = expression

    def __eq__(self, other):
        if not isinstance(other, Filter):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__expression == other.get_expression()

    def get_expression(self) -> Expression:
        return self.__expression

    def set_expression(self, expression: Expression):
        self.__expression = expression

    def where_condition(self, field: str, op: Operator, value) -> "Filter":
        self.__expression = Condition(field=field, op=op, value=value)
        return self

    def where_expression(self, expression: Expression) -> "Filter":
        self.__expression = expression
        return self

    def and_condition(self, field: str, op: Operator, value) -> "Filter":
        if self.__expression == None:
            raise Exception("Cannot create a conjunction for an empty expression.")
        left = self.__expression
        right = Condition(field=field, op=op, value=value)
        self.__expression = Conjunction(left, right)
        return self

    def and_expression(self, expression: Expression) -> "Filter":
        if self.__expression == None or expression == None:
            raise Exception("Cannot create a conjunction for an empty expression.")
        left = self.__expression
        self.__expression = Conjunction(left, expression)
        return self

    def and_filter(self, filter: "Filter") -> "Filter":
        if (
            self.__expression == None
            or filter == None
            or filter.get_expression() == None
        ):
            raise Exception("Cannot create a conjunction for an empty expression.")
        left = self.__expression
        self.__expression = Conjunction(left, filter.get_expression())
        return self

    def or_condition(self, field: str, op: Operator, value) -> "Filter":
        if self.__expression == None:
            raise Exception("Cannot create a disjunction for an empty expression.")
        left = self.__expression
        right = Condition(field=field, op=op, value=value)
        self.__expression = Disjunction(left, right)
        return self

    def or_expression(self, expression: Expression) -> "Filter":
        if self.__expression == None or expression == None:
            raise Exception("Cannot create a disjunction for an empty expression.")
        left = self.__expression
        self.__expression = Disjunction(left, expression)
        return self

    def or_filter(self, filter: "Filter") -> "Filter":
        if (
            self.__expression == None
            or filter == None
            or filter.get_expression() == None
        ):
            raise Exception("Cannot create a disjunction for an empty expression.")
        left = self.__expression
        self.__expression = Disjunction(left, filter.get_expression())
        return self

    def build_query(self) -> str:
        if self.__expression == None:
            return ""
        return self.__expression.build_query()

    def build_url_encoded_query(self) -> str:
        return urllib.parse.quote_plus(self.build_query())
