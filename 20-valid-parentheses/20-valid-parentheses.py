class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            if c == '(' or c=='{' or c=='[':
                stack+=c
                continue
            
            if c == ')' and stack and stack[-1]=='(':
                stack = stack[:-1]
            elif c == ']' and stack and stack[-1]=='[':
                stack = stack[:-1]
            elif c=='}' and stack and stack[-1]=='{':
                stack = stack[:-1]
            else:
                return False
        
        return not bool(stack)