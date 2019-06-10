
def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """

    while len(intervals) > 1:
        pos = 0
        for interval in intervals:
            if newInterval[1] < interval[0]:
                return intervals.insert(0, newInterval)
            elif newInterval[0] >= interval[0] and newInterval[1] <= interval[1]:
                return intervals
            elif newInterval[0] < interval[0] and newInterval[1] < interval[1]:
                intervals[pos][0] = newInterval[0]
                return intervals
            elif newInterval[0] > interval[0] and newInterval[1] > interval[1]:
                newInterval[0] = interval[0]
                intervals[pos][1] = newInterval[1]
                pos = pos + 1
            elif newInterval[0] > interval[1]:
                return intervals.append(newInterval)
            else:
                pass

        return intervals






