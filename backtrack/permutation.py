from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(permutation):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for n in nums:
                if n not in permutation:
                    permutation.append(n)
                    backtrack(permutation)
                    permutation.pop()
        backtrack([])
        return res
        