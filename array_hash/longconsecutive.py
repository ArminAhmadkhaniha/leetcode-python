class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        longest = 0
        for n in numbers:
            if (n-1) not in numbers:
                length = 1
                while (n + length) in numbers:
                    length += 1
                longest = max(length, longest)
        return longest 

