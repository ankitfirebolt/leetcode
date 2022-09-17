class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        
        
        self.memoization = {}

        
        def calculate(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            if n-1 not in self.memoization:
                self.memoization[n-1] = calculate(n-1)

            if n-2 not in self.memoization:
                self.memoization[n-2] = calculate(n-2)
            return self.memoization[n-1] + self.memoization[n-2]                

        return calculate(n)