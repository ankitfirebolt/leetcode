class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        def helper(s, wordDict, memo={}):
            if not s or s in wordDict:
                return True

            if s in memo:
                return memo[s]

            for i in range(1, len(s)+1):
                if (s[:i] in wordDict): 
                    memo[s[i:]] = helper(s[i:], wordDict)
                    if memo[s[i:]]:
                        return True
        
            return False
        
        return helper(s, wordDict)