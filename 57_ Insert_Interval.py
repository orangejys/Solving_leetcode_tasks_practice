class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start, end = newInterval
        n = len(intervals)
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][1] < start:
                left = mid + 1
            else:
                right = mid
        
        lower_bound = left


        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] <= end:
                left = mid + 1
            else:
                right = mid
        
        upper_bound = left


        if lower_bound < upper_bound:

            start = min(start, intervals[lower_bound][0])
            end = max(end, intervals[upper_bound - 1][1])
        
        return intervals[:lower_bound] + [[start, end]] + intervals[upper_bound:]


    