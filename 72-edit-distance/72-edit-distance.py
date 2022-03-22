class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        m, n = len(word1), len(word2)
        dp_matrix = [[0]*(n+1) for i in range(m+1)]
        
        
        #initialize base cases
        for i in range(m+1):
            dp_matrix[i][0] = i
        for j in range(n+1):
            dp_matrix[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                min_strategy = min(dp_matrix[i-1][j], dp_matrix[i-1][j-1], dp_matrix[i][j-1])
                if word1[i-1] == word2[j-1]: #because i-1 and j-1 are the index of the characters
                    dp_matrix[i][j] = dp_matrix[i-1][j-1]
                else:
                    dp_matrix[i][j] = 1 + min_strategy
        return dp_matrix[m][n]
    
    def minDistance_Recursion_Memoization(self, word1, word2, memo = {}):
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
            memo[(word1, word2)] = self.minDistance_Recursion_Memoization(word1[1:], word2[1:], memo)
            return memo[(word1, word2)]
        else:
            #insert
            insert_path = 1 + self.minDistance_Recursion_Memoization(word1, word2[1:], memo)

            #delete
            delete_path = 1 + self.minDistance_Recursion_Memoization(word1[1:], word2, memo)
            
            #replace
            replace_path = 1 + self.minDistance_Recursion_Memoization(word1[1:], word2[1:], memo)
            
            memo[(word1, word2)] = min(insert_path, delete_path, replace_path)
            return memo[(word1, word2)]