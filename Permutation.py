class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(newNums, container, ans):
            if not newNums:
                ans.append(container)
            for i in range(len(newNums)):
                backtrack(newNums[:i]+newNums[i+1:], container+[newNums[i]], ans)
                
        ans = []
        container = []
        backtrack(nums, container, ans)
        
        return ans
            