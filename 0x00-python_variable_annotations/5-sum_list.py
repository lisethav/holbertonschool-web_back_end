#!/usr/bin/env python3
"""5. Complex types - list of floats"""

from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sum_list which takes a list input_list 
    of floats as argument and returns their sum as a float."""
    return reduce(lambda a, b: a+b, input_list)