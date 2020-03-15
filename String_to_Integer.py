class Solution:
    def myAtoi(self, str: str) -> int:
        ls = list(str.strip())
        
        if len(ls) == 0:
            return 0
        
        sign = -1 if ls[0] == '-'else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + ord(ls[i]) - ord('0') #int(ls[i]) is fine as well but slower than ord()
            i += 1
        return max(-2**31, min(sign * ret, 2**31-1))
        