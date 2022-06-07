#!/usr/bin/env python3
"""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function make_multiplier that takes a float multiplier as argument """
    def multi(x: float) -> float:
        """returns a function that multiplies a float by multiplier."""
        return multiplier * x

    return multi
