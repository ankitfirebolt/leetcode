class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod = {} #product upto i, not including i
        right_prod = {} #product upto i in reverse, not including i
        
        prod = 1
        answer = []
        
        for i, n in enumerate(nums):
            left_prod[i] = prod
            prod = prod*n
            
        prod = 1
        for i,n in enumerate(nums[::-1]):
            right_prod[len(nums)-1-i] = prod
            prod = prod*n
            
        print(left_prod)
        print(right_prod)
        answer = [left_prod[i] * right_prod[i] for i in range(len(nums))]
        
        return answer