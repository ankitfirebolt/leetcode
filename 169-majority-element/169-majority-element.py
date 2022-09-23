class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        curr_major = nums[0]
        count = 1
        
        for n in nums[1:]:
            if n == curr_major:
                count+=1
            else:
                count-=1
            
            if count < 0:
                curr_major = n
                count = 1
                
        return curr_major
        
        