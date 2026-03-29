from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        
        head_res = ListNode(0)   
        res = head_res
        
        carry = 0

        # loop while BOTH exist
        while head1 and head2:
            total = head1.val + head2.val + carry
            
            carry = total // 10
            digit = total % 10
            
            res.next = ListNode(digit)   
            res = res.next
            
            head1 = head1.next
            head2 = head2.next

        # remaining l1
        while head1:
            total = head1.val + carry
            
            carry = total // 10
            digit = total % 10
            
            res.next = ListNode(digit)
            res = res.next
            
            head1 = head1.next

        # remaining l2
        while head2:
            total = head2.val + carry
            
            carry = total // 10
            digit = total % 10
            
            res.next = ListNode(digit)
            res = res.next
            
            head2 = head2.next

        # leftover carry
        if carry:
            res.next = ListNode(carry)

        return head_res.next   