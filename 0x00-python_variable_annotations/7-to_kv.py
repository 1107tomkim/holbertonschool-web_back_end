#!/usr/bin/env python3
"""Type annotated func"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return val tuples as tuples where val squared"""
    return (k, v ** 2)
