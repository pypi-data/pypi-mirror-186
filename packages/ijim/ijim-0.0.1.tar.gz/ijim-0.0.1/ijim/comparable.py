from abc import ABCMeta, abstractmethod
from typing import Any


class Comparable(metaclass=ABCMeta):
    """Supports `==`, `<`, `<= operators"""
    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
    @abstractmethod
    def __le__(self, other: Any) -> bool: ...
