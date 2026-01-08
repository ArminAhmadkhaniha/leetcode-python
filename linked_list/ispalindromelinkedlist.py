from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# O(1) memory and O(n) runtime       
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
        
# O(N) memory and runtime       
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []
#         cur = head
#         while cur:
#             arr.append(cur.val)
#             cur = cur.next
#         left , right = 0 , len(arr) - 1
#         while left < right:
#             if arr[left] != arr[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

