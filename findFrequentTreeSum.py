# https://leetcode.com/problems/most-frequent-subtree-sum/

from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return 0
            else:
                leftsum = dfs(node.left)
                rightsum = dfs(node.right)
                res.append(node.val + leftsum + rightsum)
                return (node.val + leftsum + rightsum)
                
        dfs(root)
        cdict = Counter(res)
        maxfreq = 0
        res = []
        for key in cdict:
            if cdict[key] > maxfreq:
                res = [key]
                maxfreq = cdict[key]
            elif cdict[key] == maxfreq:
                res.append(key)
        
        return res
        
