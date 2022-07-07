# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(i,j,k):
            if (i,j,k) not in dp:
                if i + j == len(s1) + len(s2):
                    dp[(i,j,k)] = True
                elif (i == len(s1)) != (j == len(s2)):
                    dp[(i,j,k)] = s1[i:] + s2[j:] == s3[k:]
                else:
                    dp[(i,j,k)] = (s1[i] == s3[k] and dfs(i+1, j, k+1)) or (s2[j] == s3[k] and dfs(i, j+1, k+1))


            return dp[(i,j,k)]

        return dfs(0,0,0)
        
