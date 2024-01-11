#!/usr/bin/env python3
""" Module for complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns function that multiplies a float by multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
