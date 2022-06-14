# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(curr,last):
            if not last:
                res.append(curr)
            else:
                for i in range(len(last)):
                    temp = curr + [last[i]]
                    helper(temp, last[:i] + last[i+1:])
        
        helper([],nums)
        return res
