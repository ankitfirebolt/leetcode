class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = dict()
        
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in complement_dict:
                return [complement_dict[complement], i]
            else:
                complement_dict[n] = i