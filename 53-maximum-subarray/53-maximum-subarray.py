class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr_sum = nums[0]
        for n in nums[1:]:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum