class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashset = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashset:
                return [hashset[diff], index]
            hashset[num] = index

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))



        
            
        