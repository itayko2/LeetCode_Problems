# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        def helper(vals):
            if (len(vals) <= 1):
                return vals
            else:
                if (vals[0][0] <= vals[1][0] <= vals[0][1]):
                    merged = [vals[0][0], max(vals[1][1],vals[0][1])]
                    return helper([merged] + vals[2:])
                else:
                    return [vals[0]] + helper(vals[1:])

        return helper(sorted_intervals)

            
