#!/usr/bin/env python3
"""Type annotated func"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all of float and int and return val"""
    return sum(mxd_lst)
