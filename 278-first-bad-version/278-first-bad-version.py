# The isBadVersion API is already defined for you.
# def v(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 1, n
        
        while left <= right:
            mid = (left+right)//2
            
            if left == right:
                return mid
            elif not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        
        return mid
                    
            
            