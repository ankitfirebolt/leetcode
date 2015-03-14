class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        k = 5 #Denotes power of 5. Initial equal to 5**0
        count=0
        while n/k > 0:
            count=count+(n/k)
            k=k*5
        return count
