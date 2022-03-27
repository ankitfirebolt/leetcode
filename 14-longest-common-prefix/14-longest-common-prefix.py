class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        ans = ""
        
        max_prefix_size = min([len(s) for s in strs])
        
        for i in range(max_prefix_size):
            tops = set([s[i] for s in strs])
            if len(tops) == 1:
                ans+=tops.pop()
            else:
                break
        return ans