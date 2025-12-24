from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        
sol = Solution()
s = ["h","e","l","l","o"]
sol.reverseString(s)
print(s)

s = ["H","a","n","n","a","h"]
sol.reverseString(s)
print(s)

s = ["a","b"]
sol.reverseString(s)
print(s)