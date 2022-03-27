class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]
        
        ans = [[1], [1,1]]

        for r in range(2, numRows):
            prev = ans[-1]
            build_row = [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)]+[1]            
            ans.append(build_row)
        
        return ans