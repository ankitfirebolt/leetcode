class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        curr_color, new_color = image[sr][sc], color
        if curr_color == new_color:
            return image #otherwise we will need to flag visited nodes to avoid infinite recursion
        
        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != curr_color:
                return
            elif image[r][c] == curr_color:
                image[r][c] = new_color
                #dfs on neighbors
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        dfs(sr, sc)
        return image