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
    STARTS_WITH = "starts with"
    ENDS_WITH = "ends with"
