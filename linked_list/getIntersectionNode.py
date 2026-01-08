from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
  
# O(n + m) runtime and O(n) memory where m is the length of the secondtlist and  n is the length of the firstlist.        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeset = set()
        cur = headA
        while cur:
            nodeset.add(cur.val)
            cur = cur.next
        cur = headB
        while cur:
            if cur in nodeset:
                return cur
            
            cur = cur.next
        return None