from typing import Iterable

from .comparable import Comparable


def is_sorted(iterable: Iterable[Comparable]) -> bool:
    """Check if `iterable` is sorted in non-decreasing order"""
    for i in range(len(iterable) - 1):
        if not iterable[i] <= iterable[i + 1]:
            return False
    return True


def has_duplicates(iterable: Iterable) -> bool:
    """Check if `iterable` has duplicated values"""
    return len(iterable) != len(set(iterable))
