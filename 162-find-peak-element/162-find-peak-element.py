class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        
        def helper(nums, i, j):
            
            if i == j:
                return i
            
            mid = int((i+j)/2)
            
            if nums[mid] < nums[mid+1]:
                return helper(nums, mid+1, j)
            else:
                return helper(nums, i, mid)
            
        return helper(nums, 0, len(nums)-1)