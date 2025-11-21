from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
        
        
# Test
from invertTree_DFS import build_tree
root = build_tree([3,9,20,None,None,15,7])
sol = Solution()
print(sol.maxDepth(root))