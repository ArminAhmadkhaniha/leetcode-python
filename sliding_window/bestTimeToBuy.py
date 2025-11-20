class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy , sell = 0 , 1
        maxprofit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprofit = max(maxprofit, profit)
            
            else:
                buy = sell
            sell += 1
        return maxprofit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([2,4,1]))
print(sol.maxProfit([2,1,2,0,1]))

        