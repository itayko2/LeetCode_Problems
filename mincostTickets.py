# https://leetcode.com/problems/minimum-cost-for-tickets/
# Medium

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mydict = {0:0}
        days_pool = set(days)
        def dfs(day):
            if day not in mydict:
                if day < 0:
                    return 0
                else:
                    if day in days_pool:
                        daily = costs[0] + dfs(day - 1)
                        weekly = costs[1] + dfs(day - 7)
                        monthly = costs[2] + dfs(day - 30)
                        mydict[day] = min(daily,weekly,monthly)
                    else:
                        mydict[day] = dfs(day - 1)
            
            return mydict[day]
        
        res = dfs(days[-1])
        return res
        
