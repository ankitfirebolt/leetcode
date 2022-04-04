class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr_max = ""
        self.global_max = ""
        
        def helper(s, i, j, curr_max):
  
            #Stopping condition
            if not s or i<0 or i >= len(s) or j < 0 or j >= len(s) or s[i] != s[j]:
                return
            
            #Base case
            if s[i] == s[j]:
                curr_max = s[i:j+1]
                
            
            if len(curr_max) > len(self.global_max):
                self.global_max = curr_max
            
            helper(s, i-1, j+1, curr_max)
                
            
            
            
        for i in range(len(s)):
            helper(s, i, i, 0) #odd palindromes
            helper(s, i, i+1, 0) #even palindromes
            
        return self.global_max