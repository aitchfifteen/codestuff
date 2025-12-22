class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best = 0

        for x in range(len(prices) - 1):
            if prices[x] < prices[x+1]:
                profit = prices[x+1] - prices[x]
                best = best + profit
        
        return best




        
    