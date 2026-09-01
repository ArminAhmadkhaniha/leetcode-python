class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = []
        if x < -9:
            return False
        
        while x:
            r = x % 10
            numbers.append(r)
            x = x // 10
        

        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] != numbers[right]:
                return False
            left += 1
            right -= 1
        
        return True
    


        