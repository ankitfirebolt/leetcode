class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        mapping = {}
        
        for i,n in enumerate(numbers):
            
            if n in mapping:
                return [mapping[n]+1, i+1]
            else:
                mapping[target-n] = i
