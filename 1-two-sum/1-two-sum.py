class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        
        for i,n in enumerate(nums):
            if n not in complements:
                complements[target-n] = i
            else:
                return [i, complements[n]]