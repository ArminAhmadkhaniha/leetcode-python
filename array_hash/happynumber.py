class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquare(n : int) -> int:
            res = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                res += digit
                n = n // 10
            return res

        visit = set()
        while n not in visit:
            visit.add(n)
            n = sumOfSquare(n)
            if n == 1:
                return True
        return False
     
    

    
        

        