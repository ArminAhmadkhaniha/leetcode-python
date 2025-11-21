from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        dummy = tail
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list1:
                dummy.next = list1
        elif list2:
                dummy.next = list2
        return tail.next


# Test
from cycle import build_list

def to_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

sol = Solution()

list1 = build_list([1, 2, 4], pos = -1)
list2 = build_list([1, 3, 4], pos = -1)

merged_head = sol.mergeTwoLists(list1, list2)

print(to_list(merged_head))   # [1, 1, 2, 3, 4, 4]   
