"""This module contains some helper functions."""

import os
import sys

from typing import List

DATA_NOT_EXTRACTED = 'Failed to extract any data from "{}"'
TITLE_NOT_BUILT = 'Failed to built title for "{}".'


def parse_file(path: str, delim: str = ',') -> List[List[str]]:
    """Read data from delim-delimited file and insert data into list."""
    values = []
    with open(path, 'r', encoding='utf-8') as fromF:
        for line in fromF:
            values.append(line.strip().split(delim))
    if not values:
        sys.exit(DATA_NOT_EXTRACTED.format(path))
    return values


def build_spreadsheet_title(filename: str) -> str:
    """Return file name without full path and extension."""
    _, tail = os.path.split(filename)
    head, _ = os.path.splitext(tail)
    if not head:
        sys.exit(TITLE_NOT_BUILT.format(filename))
    return head
