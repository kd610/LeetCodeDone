class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2*numRows - 2
        result = []
        
        for i in range(numRows):
            for j in range(i, n, cycle):
                result.append(s[j])
                if i != numRows-1 and i != 0 and (j+cycle-2*i) < n:
                    result.append(s[j+cycle-2*i])
        ans = ''.join(result)
        
        return ans