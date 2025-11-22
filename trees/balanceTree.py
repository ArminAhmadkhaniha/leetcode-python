from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                isbalance = True
            else:
                isbalance = False
            return [isbalance, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


# Test
# This can be tested using (build_tree and tree_to_list functions available in inverTree_DFS.py)
        