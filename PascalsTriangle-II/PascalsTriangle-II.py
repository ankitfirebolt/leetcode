class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        
        rowList = []
        for i in range(rowIndex+1):
            rowList.append(math.factorial(rowIndex)/(math.factorial(i)*math.factorial(rowIndex-i)))            
        return rowList
