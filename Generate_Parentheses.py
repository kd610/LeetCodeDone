class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S='', left = n, right=n):
            if len(S) == 2*n:
                print(S)
                ans.append(S)
                return
            if left > 0:
                backtrack(S+'(', left-1, right)
            if right > left:
                backtrack(S+')', left, right-1)
                
        backtrack()
        return ans