class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        english = 'abcdefghijklmnopqrstuvwxyz'
        hash_map = {}
        for i in range(len(order)):
            hash_map[order[i]] = english[i]
        
        
        def convert(word):
            return ''.join([hash_map[c] for c in word])
        
        for i in range(len(words)):
            if i == len(words)-1:
                break
                
            if convert(words[i]) > convert(words[i+1]):
                return False
        
        return True
            