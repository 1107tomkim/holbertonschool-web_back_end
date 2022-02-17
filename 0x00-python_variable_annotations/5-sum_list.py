#!/usr/bin/env python3
"""Type annotated func"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all float and return the float val"""
    return sum(input_list)
