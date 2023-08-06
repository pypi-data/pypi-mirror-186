IntervalMapUnequalLength = ValueError(
    "len of the `intervals_left_points` must be equal to len of `vals`")
IntervalMapMustBeSorted = ValueError(
    "`intervals_left_points` must be sorted in ascending order")
IntervalMapNoDuplicates = ValueError(
    "`intervals_left_points` must not contain duplicates")
