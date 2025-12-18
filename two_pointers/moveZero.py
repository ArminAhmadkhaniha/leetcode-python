from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[i] = nums[k]
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
            
            
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print(sol.moveZeroes([0]))

            
        
        
        

        