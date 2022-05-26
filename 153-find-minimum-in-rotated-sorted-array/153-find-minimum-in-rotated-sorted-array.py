class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = int((left+right)/2)
            
            if nums[left] < nums[mid] and nums[mid] > nums[right]:
                left = mid+1
            elif nums[left] > nums[mid] and nums[mid] < nums[right]:
                right = mid
            else:
                break
        return min(nums[left], nums[right])
        
        
        
        
        