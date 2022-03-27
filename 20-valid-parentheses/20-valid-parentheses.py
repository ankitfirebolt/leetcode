class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}':'{', ']': '['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack and mapping[c] == stack[-1]:
                stack.pop(-1)
            else:
                return False
            
        return not stack
                