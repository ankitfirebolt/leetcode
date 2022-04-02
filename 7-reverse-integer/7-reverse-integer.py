class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_num, sign = 0, 0
        
        sign = -1 if x<0 else +1
            
        x = x*sign #making x +ve
        
        while(x>0):
            digit = x%10
            rev_num = rev_num*10 + digit
            x=x/10
        
        if -2**31 <= sign*rev_num and sign*rev_num <= 2**31 - 1:
            return sign*rev_num
        else:
            return 0
        