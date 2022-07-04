import itertools
import typing

import pandas as pd
import numpy as np

def find_queries(rows: pd.Series, cols: pd.Series) -> typing.List[typing.List]:
    queries = []
    for x, y in itertools.product(rows.iteritems(), cols.iteritems()):
        if x[1] == y[1] and x[1]:
            queries.append([x[0], y[0]])
    return queries

def find_column_indexes(df: pd.DataFrame, queries: typing.List) -> typing.List:
    new_queries = []
    for item in queries:
        new_queries.append([item[0], df.columns.get_loc(item[1])])
        
    return new_queries
        
        
def example_sql_response() -> pd.DataFrame:
    return pd.DataFrame(
        {
            'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
            'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
            'age': [41, 28, 33, 34, 38, 31, 37],
            'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0],
        }
    )