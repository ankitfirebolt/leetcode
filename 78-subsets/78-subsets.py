class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        subs = self.subsets(nums[1:])
        
        return subs+[ [nums[0]]+s for s in subs ]
            