class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i,j = 0,0
        
        while i < len(nums) and j < len(nums):
            if nums[i] != 0:
                i+=1
                j+=1
            else:
                while(nums[j]==0 and j < len(nums)-1):
                    j+=1
                nums[i] = nums[j]
                nums[j] = 0
                i+=1
        return nums
                
        
        
        