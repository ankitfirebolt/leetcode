class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i= 0
        top = nums[0]
        
        for curr in nums[1:]:
            if curr != top:
                i+=1
                nums[i] = curr
                top = nums[i]
                
        return i+1
            
            
        