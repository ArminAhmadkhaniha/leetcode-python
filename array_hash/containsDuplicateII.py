from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        diff = 0
        for index, val in enumerate(nums):
            if val not in hashmap:
                hashmap[val] = index
            else:
                diff = abs(hashmap[val]-index)
                if diff <= k:
                    return True
                hashmap[val] = index
        return False

        