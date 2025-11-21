from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev




# Test
from cycle import build_list
from mergeSorted import to_list

sol = Solution()

head = build_list([1, 2, 3, 4, 5])
reversed_head = sol.reverseList(head)

print(to_list(reversed_head))   # [5, 4, 3, 2, 1]