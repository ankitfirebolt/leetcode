class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        def helper(coins, amount, memo={}):
            if amount == 0:
                return 0

            if amount < 0:
                return float("Inf")
            
            if amount in memo:
                return memo[amount]

            ans = float("Inf")

            for c in coins:
                memo[amount-c] = helper(coins, amount-c, memo)
                with_c = 1 + memo[amount-c]
                
                ans = min(ans, with_c)
            return ans
        
        output = helper(coins, amount)
        if output != float("Inf"):
            return output
        else:
            return -1