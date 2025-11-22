from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res
        

# Test
from invertTree_DFS import build_tree, tree_to_list

sol = Solution()
tree = build_tree([1,2,3,4,5])
print(sol.diameterOfBinaryTree(tree))