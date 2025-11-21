from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


        
        
        
# Test
# --- Helper: create linked list and optional cycle ---
def build_list(values, pos=-1):
    """
    values: list of integers
    pos: index where tail should connect to (-1 means no cycle)
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]

    if pos != -1:
        nodes[-1].next = nodes[pos]  # create cycle

    return nodes[0]


# --- Test the code locally ---
sol = Solution()

# Example 1: list with cycle [3,2,0,-4], tail connects to index 1
head1 = build_list([3, 2, 0, -4], pos=1)
print(sol.hasCycle(head1))   # True

# Example 2: list without cycle
head2 = build_list([1, 2, 3, 4], pos=-1)
print(sol.hasCycle(head2))   # False