class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i, j = 0, len(numbers)-1
        
        while(i!=j):
            if numbers[i]+numbers[j] > target: #need to reduce sum
                j-=1
            elif numbers[i]+numbers[j] < target: #need to increase sum
                i+=1
            else:
                return [i+1, j+1]