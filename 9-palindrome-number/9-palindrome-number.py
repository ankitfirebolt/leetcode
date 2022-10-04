class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = x
        reverse_num = 0
        
        while x > 0:
            reverse_num = 10*reverse_num + (x%10)
            x = x//10
        
        return num == reverse_num
        