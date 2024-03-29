class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        hash_map = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total, i = 0, 0
        while i < len(s):
            
            if i+1 < len(s) and s[i]+s[i+1] in hash_map:
                total += hash_map[s[i]+s[i+1]]
                i+=2
            else:
                total += hash_map[s[i]]
                i+=1
     
        return total