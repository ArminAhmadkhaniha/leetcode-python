from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(s)

        return list(hashmap.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))

