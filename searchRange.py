from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            first = nums.index(target)
            last = len(nums) - 1 - nums[::-1].index(target)
            return [first, last]
        else:
            return [-1, -1]
        
nums = [5,7,7,8,8,10]
target = 8  
print(Solution().searchRange(nums, target))  # Output: [3, 4]