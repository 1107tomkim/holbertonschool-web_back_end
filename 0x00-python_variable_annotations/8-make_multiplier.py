#!/usr/bin/env python3
"""Type annotated func"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that multi floats by multi is returned"""
    def multiply_by_multiplier(num: float) -> float:
        """Returns val of multi and val"""
        return multiplier * num
    return multiply_by_multiplier
