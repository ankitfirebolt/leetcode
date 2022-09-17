class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        
        i, j = 0, 0
        
        while i < len(ransomNote) and j < len(magazine):

            if ransomNote[i] == magazine[j]:
                i+=1
            
            j+=1 # go to next magazine letter
        
        if i == len(ransomNote): # we were able to make the ransom note
            return True
        else:
            return False # magazine charaters were not enough