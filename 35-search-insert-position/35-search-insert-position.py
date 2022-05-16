class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i, j = 0, len(nums)-1
        
        if target < nums[0]:
            return 0
        elif target > nums[j]:
            return j+1
        
        while i<=j:
            mid = int((i+j)/2)
            
            if target > nums[mid]:
                i = mid+1
            elif target < nums[mid]:
                j = mid-1
            else:
                return mid
            
        if target > nums[i]:
            return i+1
        elif target < nums[i]:
            return i