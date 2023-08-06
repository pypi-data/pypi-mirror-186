from typing import Literal, Union

# Filter
EQ: Literal["equals"]
NOT_EQ: Literal["doesNotEqual"]
CONTAINS: Literal["contains"]
EXCLUDES: Literal["excludes"]
GT: Literal["greaterThan"]
LT: Literal["lessThan"]
LTE: Literal["lessThanOrEqual"]
GTE: Literal["greaterThanOrEqual"]

FilterSearchType = Union[
    Literal["equals"],
    Literal["doesNotEqual"],
    Literal["contains"],
    Literal["excludes"],
    Literal["greaterThan"],
    Literal["lessThan"],
    Literal["lessThanOrEqual"],
    Literal["greaterThanOrEqual"],
]

# Aggregate
AVG: Literal["average"]
COUNT: Literal["count"]
SUM: Literal["sum"]
MIN: Literal["min"]
MAX: Literal["max"]

AggregateSearchType = Union[Literal["average"], Literal["count"], Literal["sum"], Literal["min"], Literal["max"]]

# GroupBy
GB: Literal["groupBy"]
HOUR: Literal["groupByHour"]
DAY: Literal["groupByDay"]
WEEK: Literal["groupByWeek"]
MONTH: Literal["groupByMonth"]
QUARTER: Literal["groupByQuarter"]
YEAR: Literal["groupByYear"]

GroupBySearchType = Union[
    Literal["groupBy"],
    Literal["groupByHour"],
    Literal["groupByDay"],
    Literal["groupByWeek"],
    Literal["groupByMonth"],
    Literal["groupByQuarter"],
    Literal["groupByYear"],
]

# Sorts
ASC: Literal["ascending"]
DESC: Literal["descending"]

SortSearchType = Union[Literal["ascending"], Literal["descending"]]
