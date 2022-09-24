class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        length = min([len(s) for s in strs])
        
        common_prefix = ""
        
        for i in range(length):
            local_set = set([s[i] for s in strs])
            if len(local_set) == 1:
                common_prefix += local_set.pop()
            else:
                break
                
        return common_prefix