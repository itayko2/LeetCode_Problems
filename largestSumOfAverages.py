# https://leetcode.com/problems/largest-sum-of-averages/

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        dp = [[0] * k for _ in range(len(nums))]
        def avg(lst):
            return sum(lst) / len(lst)
        
        for i in range(len(nums) -1, -1, -1):
            for j in range(k):
                if j == 0:
                    dp[i][j] = avg(nums[i:])
                elif len(nums[i:]) < j + 1:
                    dp[i][j] = 0
                elif len(nums[i:]) == j + 1:
                    dp[i][j] = sum(nums[i:])
                else:
                    for x in range(i,len(nums) - 1):
                        dp[i][j] = max(avg(nums[i:x+1]) + dp[x+1][j-1], dp[i][j])

        return dp[0][k - 1]
        
