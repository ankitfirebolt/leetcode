class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = {}
        
        for i,n in enumerate(nums):
            if target - n in hashdict:
                return [i, hashdict[target-n]]
            hashdict[n]=i
            