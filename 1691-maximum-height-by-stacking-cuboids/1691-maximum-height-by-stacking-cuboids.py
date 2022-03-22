class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Dynamic Programming definition
        # dp[i] = maximum height obtained with cuboids[i] being the base cuboid
        for cuboid in cuboids:
            cuboid.sort()
        
        cuboids.sort(key = lambda cube : (cube[0], cube[1], cube[2]))
        dp = [0 for i in range(len(cuboids))]
        dp[0] = cuboids[0][2]
        
        for i in range(1, len(cuboids)):
            best = 0
            for k in range(i):
                if all(dim1 <= dim2 for dim1, dim2 in zip(cuboids[k], cuboids[i])):
                    best = max(best, dp[k])
            dp[i] = best + cuboids[i][2]
            
        return max(dp)