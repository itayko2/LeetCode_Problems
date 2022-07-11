# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        memo = {}
        
        def dfs(curr, depth):
            if not curr:
                return
            else:
                memo[depth] = curr.val
                dfs(curr.left, depth + 1)
                dfs(curr.right, depth + 1)
            
        
        dfs(root,1)
        return [memo[x] for x in memo]
