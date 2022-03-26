class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_total = total = nums[0]
        
        
        for k in range(1, len(nums)):
            if total > max_total:
                    max_total = total
            if total < 0:
                #reset total
                total = nums[k]
            else:
                total+=nums[k]
        return max(total, max_total)