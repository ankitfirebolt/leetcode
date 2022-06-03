class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        temp_set = set()
        max_count = 0
        
        for c in s:
            
            if c in temp_set:
                while c in temp_set:
                    temp_set.remove(s[start])
                    start+=1

            temp_set.add(c)
            end+=1
            max_count = max(max_count, end-start)
        
        return max_count
            