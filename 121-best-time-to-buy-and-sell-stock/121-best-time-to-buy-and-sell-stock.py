class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_min, curr_profit, best_profit = prices[0], 0, 0
        
        for p in prices:
            curr_profit = p-curr_min
            
            if curr_profit > best_profit:
                best_profit = curr_profit
                
            if p < curr_min:
                curr_min=p
                
        return best_profit
        
        