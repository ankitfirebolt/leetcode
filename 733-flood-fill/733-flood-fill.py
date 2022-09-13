class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        curr_color = image[sr][sc]
        if curr_color == color:
            return image
        
        def dfs(image, r, c, curr_color, new_color):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != curr_color:
                return
            elif image[r][c] == curr_color:
                image[r][c] = new_color
                #dfs on neighbors
                dfs(image, r+1, c, curr_color, new_color)
                dfs(image, r-1, c, curr_color, new_color)
                dfs(image, r, c+1, curr_color, new_color)
                dfs(image, r, c-1, curr_color, new_color)


        dfs(image, sr, sc, curr_color, color)
        return image