class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        candidate, count = nums[0], 1
        
        for n in nums[1:]:
            if count == 0:
                candidate = n
                count+=1
            elif n == candidate:
                count+=1
            else:
                count-=1
                
        
        return candidate