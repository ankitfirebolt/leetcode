class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i=0
        num=0
        while n>0:
            if n%2 == 1:
                num = num + 2**(31-i)
            i=i+1
            n=n/2
            
        return num
        
