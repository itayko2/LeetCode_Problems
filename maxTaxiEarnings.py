# https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ridesDict = {i:[] for i in range(n)}
        for x in rides:
            ridesDict[x[0]].append(x)
        dp = [0] * (n + 1)
        flag = False
        for i in range(n - 1, -1, -1):
            for x in ridesDict[i]:
                flag = True
                dp[i] = max(x[2] + x[1] - x[0] + dp[x[1]],dp[i],dp[i+1])

            if not flag:
                dp[i] = dp[i+1]
            flag = False
            
        return dp[0]
        
