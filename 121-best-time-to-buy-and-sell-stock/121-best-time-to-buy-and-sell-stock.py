class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        profit = 0
        
        for p in prices:
            if p - min_so_far > profit:
                profit = p - min_so_far
            
            if p < min_so_far:
                min_so_far = p
                
        return profit