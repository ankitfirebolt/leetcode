class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        
        def helper(x):
            if not x:
                return True
            
            if x[0]!=x[-1]:
                return False
            else:
                return helper(x[1:-1])
            
        return helper(x)