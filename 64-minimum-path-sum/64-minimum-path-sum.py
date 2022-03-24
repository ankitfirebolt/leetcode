class Solution(object):
    def minPathSum(self, grid, r=0, c=0, memo={}):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(grid, r=0, c=0, memo={}):
            if r >= len(grid) or c >= len(grid[0]):
                return float("inf")

            if (r,c) in memo:
                return memo[(r,c)]

            # now we can go down or right


            cost_down = helper(grid, r+1, c, memo)

            cost_right = helper(grid, r, c+1, memo)

            cost = min(cost_down, cost_right)
            memo[(r,c)] = grid[r][c]

            if cost != float("inf"):
                 memo[(r,c)]+=cost
            return memo[(r,c)]
        return helper(grid)