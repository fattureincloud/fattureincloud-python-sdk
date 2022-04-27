from fattureincloud_python_sdk.filter.expression import Expression
from fattureincloud_python_sdk.filter.operator import Operator


class Condition(Expression):

    __value_dict = {
        bool: lambda b: "true" if b else "false",
        str: lambda s: "'{}'".format(s),
        type(None): lambda _: "null",
    }

    def __generic_func(self, value):
        return str(value)

    def __init__(self, field: str, op: Operator, value):
        self.__field = field
        self.__op = op
        self.__value = value

    def __eq__(self, other):
        if not isinstance(other, Condition):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.__field == other.get_field()
            and self.__op == other.get_op()
            and self.__value == other.get_value()
        )

    def get_field(self) -> str:
        return self.__field

    def set_field(self, field: str):
        self.__field = field

    def get_op(self) -> Operator:
        return self.__op

    def set_op(self, op: Operator):
        self.__op = op

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def build_query(self) -> str:
        f = self.__value_dict.setdefault(type(self.__value), self.__generic_func)
        return "{} {} {}".format(self.__field, self.__op.value, f(self.__value))
