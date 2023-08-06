from typing import Iterable

from .comparable import Comparable


def is_sorted(iterable: Iterable[Comparable]) -> bool:
    for i in range(len(iterable) - 1):
        if not iterable[i] <= iterable[i + 1]:
            return False
    return True


def has_duplicates(iterable: Iterable) -> bool:
    return len(iterable) != len(set(iterable))
