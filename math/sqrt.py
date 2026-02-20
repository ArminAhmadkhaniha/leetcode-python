class Solution:
    def mySqrt(self, x: int) -> int:
        
        res = 0
        left = 0
        right = x 
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                res = mid
                left = mid + 1
            else:
                return mid
        return res 



        