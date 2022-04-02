class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(r, c, board, word):    
            if word == "":
                return True
            
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or word[0]!=board[r][c]: #overshot or no-match or already-visited (0 will never match word[0] as it's int)
                return False
            
            board[r][c] = 0 #marking visited
            
            if helper(r+1, c, board, word[1:]) or helper(r-1, c, board, word[1:]) or helper(r, c+1, board, word[1:]) or helper(r, c-1, board, word[1:]):
                return True
            else:
                board[r][c] = word[0] #reverting the change. This is very important
                return False
            
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if helper(r, c, board, word):
                    return True
                
        return False