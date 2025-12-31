from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        
        rev = reverse(head)

        
        if n == 1:
            rev = rev.next
        else:
            cur = rev
            for _ in range(n - 2):
                cur = cur.next
            cur.next = cur.next.next

        
        return reverse(rev)

