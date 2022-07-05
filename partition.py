# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        
        def pal(p):
            return p == p[::-1]
        
        def dfs(curr, i):
            if i == n:
                res.append(curr)
                return
            else:
                for k in range(i+1,n+1):
                    if pal(s[i:k]):
                        dfs(curr + [s[i:k]], k)
        
        dfs([],0)
        return res
