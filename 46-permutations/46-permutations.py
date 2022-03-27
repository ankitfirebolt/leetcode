class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 1:
            return [nums]
        
        permutations = self.permute(nums[1:])
        ans = []
        for p in permutations:
            ans = ans + [p[0:i]+[nums[0]]+p[i:] for i in range(len(p)+1)]
        
        return ans