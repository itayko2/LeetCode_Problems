# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# 'hard' question

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        m = len(matrix)
        dp = [[-1] * (n+2) for _ in range(m+2)]
        adjList = {}
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = matrix[i][j]
        
        for i in range(m):
            for j in range(n):
                adjList[(i,j)] = []
                if dp[i+1][j+1] < dp[i+1][j+2]:
                    adjList[(i,j)].append((i,j+1))
                if dp[i+1][j+1] < dp[i+2][j+1]:
                    adjList[(i,j)].append((i+1,j))
                if dp[i+1][j+1] < dp[i+1][j]:
                    adjList[(i,j)].append((i,j-1))
                if dp[i+1][j+1] < dp[i][j+1]:
                    adjList[(i,j)].append((i-1,j))
                    
        dp = [[0] * (n) for _ in range(m)]
        
        def dfs(i,j):
            if dp[i][j] == 0:
                if not adjList:
                    dp[i][j] = 1
                else:
                    for (a,b) in adjList[i,j]:
                        dp[i][j] = max(dp[i][j],1 + dfs(a,b))
            return dp[i][j]   
                                       
        for i in range(m):
            for j in range(n):
                dp[i][j] = dfs(i,j)

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,dp[i][j])
        return res + 1
            
