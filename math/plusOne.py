from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
    
    
sol = Solution()
print(sol.plusOne([9, 9, 9]))

        
# def plusOne(self, digits: List[int]) -> List[int]:
    
#     n = len(digits) - 1
#     res = 1
#     digitslist = []
#     while n >= 0:
#         for num in digits:
#             res += num * (10 ** n)
#             n -= 1

#     while res > 0:
#         digitslist.append(res % 10)
#         res //= 10
#     return digitslist[::-1]
        
# O(n^2) run time complexity
# O(n) space complexity
# the commented code