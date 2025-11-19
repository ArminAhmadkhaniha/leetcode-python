class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if self.isalpha(s[left]) and self.isalpha(s[right]):
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            elif not self.isalpha(s[left]):
                left += 1
            else:
                right -= 1
        return True 

    def isalpha(self,ch):
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9') )
        

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
print(sol.isPalindrome("0P"))
print(sol.isPalindrome(".,"))
print(sol.isPalindrome("ab2a"))