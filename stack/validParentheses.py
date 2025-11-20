class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            if ch in hashmap:
                stack.append(ch)
            else:
                if not stack or ch != hashmap[stack[-1]]:
                    return False
                stack.pop()

        return len(stack) == 0

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
                
                 


