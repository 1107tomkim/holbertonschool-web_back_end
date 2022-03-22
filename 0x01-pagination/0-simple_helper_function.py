#!/usr/bin/env python3
"""Pagination functions"""
from typing import Tuple, Union


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    """Function that returns start index and end index"""
    if page == 0 and page_size:
        end_index = page_size
        start_index = 0
        return (start_index, end_index)
    if page and page_size:
        end_index = page * page_size
        start_index = end_index - page_size
        return(start_index, end_index)
    return None
