class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        rev_a = a[::-1]
        rev_b = b[::-1]
        
        # make sure rev_a is longer
        if len(rev_b) > len(rev_a):
            rev_a, rev_b = rev_b, rev_a
        
        #padding with zeros
        rev_b += ((len(rev_a) - len(rev_b))*'0')
        rev_ans = ""
        carry = 0
        for i in range(len(rev_a)):
            total = int(rev_a[i]) + int(rev_b[i]) + carry
            if total == 0 or total == 1:
                carry = 0
                rev_ans += str(total)
            elif total == 2:
                carry = 1
                rev_ans += '0'
            else:
                carry = 1
                rev_ans += '1'
        if carry:
            rev_ans += '1'
        
                
                
        return rev_ans[::-1]