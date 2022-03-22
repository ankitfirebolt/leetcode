class Solution(object):
    def minDistance(self, word1, word2, memo = {}):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if (word1,word2) in memo:
            return memo[(word1,word2)]
        
        if word1 == "":
            return len(word2)
        
        if word2 == "":
            return len(word1)
        
        if word1[0] == word2[0]:
            memo[(word1, word2)] = self.minDistance(word1[1:], word2[1:], memo)
            return memo[(word1, word2)]
        else:
            #insert
            insert_path = 1 + self.minDistance(word1, word2[1:], memo)

            #delete
            delete_path = 1 + self.minDistance(word1[1:], word2, memo)
            
            #replace
            replace_path = 1 + self.minDistance(word1[1:], word2[1:])
            
            memo[(word1, word2)] = min(insert_path, delete_path, replace_path)
            return memo[(word1, word2)]