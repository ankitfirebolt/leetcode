class Solution:
    def reverseBits(self, n: int) -> int:

        last_digit, ans = 0, 0
        for i in range(0,32):
            last_digit = n & 1 # n % 2
            ans = (ans << 1) + last_digit #(2*ans) + last_digit
            n = n >> 1 # n // 2
        
        return ans