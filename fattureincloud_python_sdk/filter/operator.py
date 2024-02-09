import enum


class Operator(enum.Enum):
    EQ = "="
    GT = ">"
    GTE = ">="
    LT = "<"
    LTE = "<="
    NEQ = "<>"
    IS = "is"
    IS_NOT = "is not"
    LIKE = "like"
    CONTAINS = "contains"
    NOT_LIKE = "not like"
    NOT_CONTAINS = "not contains"
    STARTS_WITH = "starts with"
    ENDS_WITH = "ends with"
