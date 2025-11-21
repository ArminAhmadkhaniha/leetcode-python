
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Test
from collections import deque

# --- Helper: build tree from list like LeetCode ---
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# --- Helper: print tree (level-order) ---
def tree_to_list(root):
    if not root:
        return []
    output = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            output.append(None)
    # Remove trailing None values
    while output and output[-1] is None:
        output.pop()
    return output


sol = Solution()
tree = build_tree([4,2,7,1,3,6,9])
inverted = sol.invertTree(tree)
print(tree_to_list(inverted))

