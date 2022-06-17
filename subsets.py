# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        pool = set()
        def helper(currSubset, leftNums):
            res.append(currSubset)
            if not leftNums:
                return
            else:
                for i in range(len(leftNums)):
                    helper(currSubset + [leftNums[i]], leftNums[i+1:])
        
        
        helper([],nums)
        return res
