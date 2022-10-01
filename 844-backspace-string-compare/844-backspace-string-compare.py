class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:        
        
    
        def calculate_resultant(s):
            stack = []
            for c in s:
                if c!='#':
                    stack.append(c)
                elif stack:
                    stack = stack[:-1]
            return stack
        return calculate_resultant(s) == calculate_resultant(t)