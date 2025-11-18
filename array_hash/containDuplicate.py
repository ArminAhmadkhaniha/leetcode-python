class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
    
    
sol = Solution()
print(sol.hasDuplicate([1,2,3,1]))