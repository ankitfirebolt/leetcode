class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        major=num[0]
        majorCount=0
        for x in num:
            if x==major:
                majorCount=majorCount+1
            else:
                majorCount=majorCount-1
            if majorCount<0:
                major=x
                majorCount=0
        return major
        
