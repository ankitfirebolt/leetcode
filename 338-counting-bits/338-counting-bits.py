class Solution:
    def countBits(self, n: int) -> List[int]:
        
        self.memoization = {}
        ans = [0]*(n+1)
        
        def count(n):
            if n == 0:
                return 0
            elif n in self.memoization:
                return self.memoization[n]
            
            if n % 2 == 1:
                self.memoization[n] = 1 + count(n//2)
            else:
                self.memoization[n] = count(n//2)
            return self.memoization[n]
            
            
        for i in range(n+1):
            ans[i] = count(i)
        
        return ans