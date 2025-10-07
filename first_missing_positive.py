from typing import List
def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    
    # Step 1: Clean up the array
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark presence
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1
        
print(firstMissingPositive(None, [3,4,-1,1]))  # Output: 2



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)  # O(n) conversion
        n = len(nums)
        
        # Check from 1 upwards
        for i in range(1, n + 1):  # include n+1 case
            if i not in nums:
                return i


print(Solution().firstMissingPositive([7,8,9,11,12]))  # Output: 2


