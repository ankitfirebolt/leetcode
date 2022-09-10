class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_so_far = prices[0]
        max_profit = 0
        curr_profit = 0
        
        for p in prices:
            min_so_far = min(min_so_far, p)
            curr_profit = p-min_so_far
            if curr_profit > max_profit:
                max_profit = curr_profit
                
        return max_profit