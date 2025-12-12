from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        res = 0
        for number in nums:
            if number == res:
                count +=1
            elif count > 0:
                count -= 1
            else:
                count = 0
                res = number
        return res
                 


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hashmap = {}
#         n = len(nums)
#         for number in nums:
#             hashmap[number] = 1 + hashmap.get(number, 0)
        
#         for key, val in hashmap.items():
#             if val >= n // 2:
#                 return key





        