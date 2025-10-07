from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def per(nums, start=0):
            n = len(nums)           

            if start == n:
                result.add(tuple(nums))
                return
            
            for i in range (start, n):
                nums[start], nums[i] = nums[i], nums[start]
                per(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]
        per(nums)

        return [list(p) for p in result]
        
sol = Solution()
print(sol.permuteUnique([1, 1, 3]))