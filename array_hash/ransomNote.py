class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for i in range(len(ransomNote)):
           
            hashmap1[ransomNote[i]] = 1 + hashmap1.get(ransomNote[i], 0)

        for j in range(len(magazine)):
            hashmap2[magazine[j]] = 1 + hashmap2.get(magazine[j], 0)

        for idx in hashmap1:
            if hashmap1[idx] > hashmap2.get(idx, 0):
                return False
        return True

            
        