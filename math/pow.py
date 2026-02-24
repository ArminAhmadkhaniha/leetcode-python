class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if x == 0:
            return 0
        res = 1
        exponent = abs(n)
        while exponent:
            if exponent % 2:
                res *= x
                exponent -= 1
            x *= x
            exponent /= 2
        
        return res if n >= 0 else 1 / res


        

        