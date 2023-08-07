from __future__ import annotations
import copy
import bisect
from pprint import pformat
from typing import Iterable, Generic, TypeVar

from .comparable import Comparable
from .utils import (
    is_sorted,
    has_duplicates,
)
from .exceptions import (
    IntervalMapUnequalLength,
    IntervalMapMustBeSorted,
    IntervalMapNoDuplicates,
)


ComparableKey = TypeVar("ComparableKey", bound=Comparable)
AnyValueType = TypeVar("AnyValueType")


class IntervalMap(Generic[ComparableKey, AnyValueType]):
    """IntervalMap maps value to some interval.
    It has default left value.

    Args:
        Generic (ComparableKey, AnyValueType): key and value types
        
    Example:
        (-inf, 1) -> 0
        
        [1, 4) -> 3
        
        [4, 7) -> 10
        
        [7, +inf) -> 17
    """
    def __init__(
        self,
        default_val: AnyValueType,
        interval_left_points: Iterable[ComparableKey] = [],
        vals: Iterable[AnyValueType] = [],
    ) -> None:
        """Interval map

        Args:
            default_val (AnyValueType): the leftmost value
            interval_left_points (Iterable[ComparableKey], optional): 
            iterable of left points of intervals. Defaults to [].
            vals (Iterable[AnyValueType], optional): 
            iterable of values which match in order to left points.
            Defaults to [].

        Raises:
            IntervalMapNoDuplicates: points must not have duplicates
            IntervalMapMustBeSorted: points must be sorted in ascending order
            IntervalMapUnequalLength: points length and vals length must be equal
        """
        if has_duplicates(interval_left_points):
            raise IntervalMapNoDuplicates
        if not is_sorted(interval_left_points):
            raise IntervalMapMustBeSorted
        if len(interval_left_points) != len(vals):
            raise IntervalMapUnequalLength

        self._lpoints = list(copy.deepcopy(interval_left_points))
        self._vals = [copy.deepcopy(default_val)] + list(copy.deepcopy(vals))
        
        for i in range(len(self._lpoints) - 1, -1, -1):
            if self._vals[i + 1] == self._vals[i]:
                self.__delete_by_index(i)
            
    def __delete_by_index(self, ind: int) -> bool:
        if ind < len(self._lpoints):
            del self._lpoints[ind]
            del self._vals[ind + 1]
            return True
        return False

    def __getitem__(self, key: ComparableKey) -> AnyValueType:
        return self.get(key)

    def get(self, key: ComparableKey) -> AnyValueType:
        """Find interval which fits the `key` and return its
        mapped value

        Args:
            key (ComparableKey)

        Returns:
            AnyValueType
        """
        return self._vals[bisect.bisect(self._lpoints, key)]

    def __setitem__(self, key: ComparableKey, val: AnyValueType) -> None:
        self.set(key, val)

    def set(self, key: ComparableKey, val: AnyValueType) -> None:
        """Set new or reset interval value

        Args:
            key (ComparableKey): new intreval key
            val (AnyValueType): new value
        """
        ind = bisect.bisect_left(self._lpoints, key)

        if ind == len(self._lpoints):
            if self._vals[ind] != val:
                self._lpoints.append(key)
                self._vals.append(val)
            return

        if self._lpoints[ind] == key:
            if self._vals[ind] != val:
                self._vals[ind + 1] = val
            else:
                self.__delete_by_index(ind)
        elif self._vals[ind] != val:
            self._lpoints.insert(ind, key)
            self._vals.insert(ind + 1, val)

    def __delitem__(self, key: ComparableKey) -> None:
        self.unset(key)

    def unset(self, key: ComparableKey) -> bool:
        """Unset interval

        Args:
            key (ComparableKey): interval left point

        Returns:
            bool: True if interval was unset, False if there is no 
            such interval left point
        """
        ind = bisect.bisect_left(self._lpoints, key)

        if ind >= len(self._lpoints):
            return False
        elif self._lpoints[ind] == key:
            self.__delete_by_index(ind)
            
            if (
                ind < len(self._vals) - 1
                and
                self._vals[ind] == self._vals[ind + 1]
            ):
                self.__delete_by_index(ind)
            
            return True
        return False

    def slice_add(
        self,
        start: ComparableKey,
        end: ComparableKey | None,
        summand: AnyValueType,
    ) -> None:
        """Add `summand` to all values in `[start, end)`

        Args:
            start (ComparableKey)
            end (ComparableKey | None)
            summand (AnyValueType)
        """
        if end is not None:
            if start > end:
                return

            end_ind = bisect.bisect(self._lpoints, end)
            val = self._vals[end_ind]

        start_ind = bisect.bisect_left(self._lpoints, start)

        if (
            start_ind == 0 
            and 
            len(self._lpoints) > 0 
            and 
            start < self._lpoints[0]
        ):
            val_ind = 0
        else:
            val_ind = start_ind + int(
                start_ind < len(self._lpoints)
                and
                start == self._lpoints[start_ind]
            )
            val_ind = val_ind if val_ind < len(self._vals) else 0

        self.set(start, self._vals[val_ind] + summand)
        start_ind = bisect.bisect(self._lpoints, start)

        if end is not None:
            end_ind = bisect.bisect_left(self._lpoints, end)
        else:
            end_ind = len(self._vals) - 1

        for ind in range(start_ind + 1, end_ind + 1):
            self._vals[ind] += summand

        if end is not None:
            self.set(end, val)

    def slice_sub(
        self,
        start: ComparableKey,
        end: ComparableKey,
        subtrahend: AnyValueType,
    ) -> None:
        """Subtract `subtrahend` from all values in `[start, end)`

        Args:
            start (ComparableKey)
            end (ComparableKey | None)
            subtrahend (AnyValueType)
        """
        self.slice_add(start, end, -subtrahend)

    def add(self, other: IntervalMap | AnyValueType) -> None:
        """Add `other` map or add some value to all intervals (
        doesn't effect default map value) inplace

        Args:
            other (IntervalMap | AnyValueType)
        """
        if isinstance(other, IntervalMap):
            for i in range(len(other._lpoints) - 1):
                self.slice_add(
                    other._lpoints[i],
                    other._lpoints[i + 1],
                    other[other._lpoints[i]]
                )
            if len(other._lpoints) > 0:
                self.slice_add(other._lpoints[-1], None, other._vals[-1])
        else:
            for i in range(1, len(self._vals)):
                self._vals[i] += other

    def sub(self, other: IntervalMap | AnyValueType) -> None:
        """Subtract `other` map or subtract some value from all intervals (
        doesn't effect default map value) inplace

        Args:
            other (IntervalMap | AnyValueType)
        """
        self.add(-other)

    def __neg__(self) -> IntervalMap:
        im = self.copy()

        for i in range(1, len(im._vals)):
            im._vals[i] *= -1

        return im

    def __str__(self) -> str:
        return (
            pformat(self.to_dict(), sort_dicts=False)
            .replace('(', '[')
            .replace('[None', '(-inf')
            .replace('None]', '+inf)')
            .replace('None)', '+inf)')
        )

    def to_dict(
        self,
    ) -> dict[tuple[ComparableKey, ComparableKey], AnyValueType]:
        """Convert `IntervalMap` to `dict`"""
        return {k: v for k, v in self}

    def __iter__(self) -> IntervalMap:
        self.__iter = -1
        self.__len = len(self._lpoints) - 1
        return self

    def __next__(
        self,
    ) -> tuple[tuple[ComparableKey, ComparableKey], AnyValueType]:
        if self.__iter == -1:
            result = (
                (
                    None,
                    self._lpoints[0] if self.__len > -1 else None
                ),
                self._vals[0]
            )
        elif self.__iter == self.__len:
            result = (
                (self._lpoints[-1], None),
                self._vals[-1]
            )
        elif self.__iter < self.__len:
            result = (
                (
                    self._lpoints[self.__iter],
                    self._lpoints[self.__iter + 1]
                ),
                self._vals[self.__iter + 1]
            )
        else:
            raise StopIteration

        self.__iter += 1
        return result

    def copy(self) -> IntervalMap:
        return copy.deepcopy(self)
