class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []
        
        ans = set()
        nums = sorted(nums)
        
        for pos,n in enumerate(nums):
            target = -n
            i=pos+1
            j=len(nums)-1
            
            while(i<j):
                if nums[i]+nums[j] > target: #decrease sum
                    j-=1
                elif nums[i]+nums[j] < target: #increase sum
                    i+=1
                else:
                    ans.add((n, nums[i], nums[j]))
                    i+=1 #either chance i or j
        return ans