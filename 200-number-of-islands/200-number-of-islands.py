class Solution(object):
    def numIslands(self, grid):
        
        #boder conditions
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1 #found an island
                    
                    # CALL EITHER BFS OR DFS
                    
                    # self.dfs(grid, i, j) #DFS  to remove all the adjacent land starting from (i,j) as root
                    
                    self.bfs(grid, i, j) #BFS  to remove all the adjacent land starting from (i,j) as root 
                    
        return count
    
    def dfs(self, grid, r, c):
        
        rows, cols = len(grid), len(grid[0])
        # border conditions
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        
        #using recursion instead of stack as they are the same mechanism
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        
    
    def bfs(self, grid, r, c): #no recursion here - will be called once per bfs
        queue = collections.deque()
        
        #initial condition: append root to queue
        queue.append((r,c))
        grid[r][c] = '0'
        
        while queue:
            r, c = queue.popleft()
            directions = [(0,1), (0,-1), (1, 0), (-1,0)]
            for d in directions:
                new_r, new_c = r + d[0] , c + d[1]
                if new_r >= 0 and new_c >= 0 and new_r < len(grid) and new_c < len(grid[0]) and grid[new_r][new_c] == '1':
                    grid[new_r][new_c] = '0'
                    queue.append((new_r, new_c))
            #performing the following above if conditions are met
            # queue.append((r, c+1))
            # queue.append((r, c-1))
            # queue.append((r+1, c))
            # queue.append((r-1, c))
        
        return
        