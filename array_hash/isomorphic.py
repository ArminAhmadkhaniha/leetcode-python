class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashmapS and hashmapS[s[i]] != t[i]:
                return False
            if t[i] in hashmapT and hashmapT[t[i]] != s[i]:
                return False

            hashmapS[s[i]] = t[i]
            hashmapT[t[i]] = s[i]
        return True


sol = Solution()
print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("paper", "title"))
print(sol.isIsomorphic("badc", "baba"))
        
            
        
    
    

        
        
        

            


        