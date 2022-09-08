class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starting_brackets = {'(', '{', '['}
        ending_brackets = {')', '}', ']'}
        mapping = {')':'(', '}':'{', ']':'['}
        
        for c in s:
            if c in starting_brackets:
                stack += c
            elif (c in ending_brackets and not stack) or (c in ending_brackets and mapping[c] != stack[-1]):
                return False
            elif (c in ending_brackets and mapping[c] == stack[-1]):
                stack = stack[:-1]
        
        if stack:
            return False
        else:
            return True
                