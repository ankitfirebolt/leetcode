class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        
        netList = []
        for i in range(numRows):
            currList = []
            for j in range(i+1):
                currList.append(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
            netList.append(currList)
        return netList
