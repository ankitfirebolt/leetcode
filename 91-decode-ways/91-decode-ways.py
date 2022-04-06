class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        allow_set = set([x for x in range(1, 27)])
        
        def helper(s, memo = {}):
            
            if not s:
                return 1
            
            if int(s[0]) == 0:
                return 0
            
            if s in memo:
                return memo[s]
            
            count_1, count_2 = 0, 0
            
            if int(s[0]) in allow_set:
                count_1 = helper(s[1:], memo)
                memo[s[1:]] = count_1
            if len(s)>=2 and int(s[:2]) in allow_set:
                count_2 = helper(s[2:], memo)
                memo[s[2:]] = count_2

            return count_1 + count_2
        return helper(s)