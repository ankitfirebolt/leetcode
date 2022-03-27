class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ans = []
        
        def build_string(left, right, curr, ans):
            if left > n or right > n or right > left:
                return
            elif left == n and right == n:
                ans += [curr]
                return
            #keep building string, just put exit condition above. Harder to build string with conditionals
            build_string(left+1, right, curr+'(', ans)
            build_string(left, right+1, curr+')', ans)
        build_string(0, 0, "", ans)
        return ans
        