class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = (start+end)//2
            
            if target < nums[mid]:
                end = mid-1
                if end >= 0:
                    if nums[end] < target:
                        return end+1
                else:
                    return 0
                        
            elif target > nums[mid]:
                start = mid+1
                if start < len(nums):
                    if nums[start] > target:
                        return start
                else:
                    return len(nums)
            else:
                return mid
        