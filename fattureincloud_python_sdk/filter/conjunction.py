from fattureincloud_python_sdk.filter.expression import Expression


class Conjunction(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.__left = left
        self.__right = right

    def __eq__(self, other):
        if not isinstance(other, Conjunction):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__left == other.get_left() and self.__right == other.get_right()

    def get_left(self) -> Expression:
        return self.__left

    def set_left(self, left: Expression):
        self.__left = left

    def get_right(self) -> Expression:
        return self.__right

    def set_right(self, right: Expression):
        self.__right = right

    def build_query(self) -> str:
        return "({} and {})".format(
            self.__left.build_query(), self.__right.build_query()
        )
