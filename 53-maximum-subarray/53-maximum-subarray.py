class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_total = curr_total = nums[0]
        
        for n in nums[1:]:
            if curr_total < 0:
                curr_total = n
            else:
                curr_total += n
            
            if curr_total > max_total:
                max_total = curr_total
                
        return max_total
        
        