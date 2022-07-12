class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        mapping = {'(' : ')', '{' : '}', '[':']'}
        
        for c in s:
            #case 1: encounter an opening bracket - we simply append and move on
            if c in mapping:
                stack.append(c)
                continue
                
            #case 2: encounter a closing bracket
            # need to check if the corresponding opening bracket is the last one and if it exists
            
            if stack and mapping[stack[-1]] == c:
                stack = stack[:-1]
            else:
                return False #mismatch
            
        #case 3: avoid cases like '((((('
        return not stack
            
            
            
            
            
            