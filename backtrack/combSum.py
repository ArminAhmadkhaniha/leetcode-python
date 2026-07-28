from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur_sum, sol):
            if cur_sum == target:
                res.append(sol.copy())
                return
            if cur_sum > target or i == len(candidates):
                return
            

            backtrack(i+1, cur_sum, sol)

            sol.append(candidates[i])
            backtrack(i, cur_sum + candidates[i], sol)
            sol.pop()

        
        backtrack(0, 0, [])
        return res
