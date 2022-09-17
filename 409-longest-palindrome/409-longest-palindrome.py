class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hash_map = {}
        
        for c in s:
            if c in hash_map:
                hash_map[c] +=1
            else:
                hash_map[c] =1
                
                
        #consider all even counts and odd counts can be converted to even (count one less). But keep the largest odd count.
        
        odd_flag = 0
        longest_palindrome = 0
        for count in hash_map.values():
            if count % 2 == 0:
                longest_palindrome += count
            else:
                longest_palindrome += (count-1) #make it even
                odd_flag = 1 #at least one odd present
        
        if odd_flag: #if there is at least one odd count
            return longest_palindrome+1
        else:
            return longest_palindrome