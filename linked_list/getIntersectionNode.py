from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
  
# O(n + m) runtime and O(n) memory where m is the length of the secondtlist and  n is the length of the firstlist.        
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         nodeset = set()
#         cur = headA
#         while cur:
#             nodeset.add(cur.val)
#             cur = cur.next
#         cur = headB
#         while cur:
#             if cur in nodeset:
#                 return cur
            
#             cur = cur.next
#         return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n + m) runtime and O(1) memory
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        countA = 0
        countB = 0
        while a:
            countA += 1
            a = a.next
        a = headB
        while a:
            countB += 1
            a = a.next
        c = headA
        d = headB
        if countA > countB:
            diff = countA - countB
            while diff > 0:
                diff -= 1
                c = c.next
            
        else:
            diff = countB - countA
            while diff > 0:
                diff -= 1
                d = d.next
        while c != d:
            c = c.next
            d = d.next
        return c



        
        


        
        

        