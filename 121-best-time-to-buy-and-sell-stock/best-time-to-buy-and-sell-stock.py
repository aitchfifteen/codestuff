class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        best = 0
        for i in prices:
            if i < min:
                min = i
            else:
                best = max(best, i - min)
        return best



            

            
            
        




    

